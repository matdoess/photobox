from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import mainthread

import os
os.environ["KIVY_IMAGE"]="pil"

from functools import partial
from time import sleep

from Helper import Helper
from SendEmail import SendEmail
from Camera import Camera
from ImageResize import ImageResize

import threading

# Screens definieren
class MenuScreen(Screen):
    pass

class SendEmailScreen(Screen):

    helper = Helper()
    mail = SendEmail()

    # Wird aufgerufen sobald sich im Textfeld etwas aendert
    # schraenkt dann die auswahl der bereits vorhandenen Mailadressen ein
    def inputChanged(self, text, *args):

        mailAddresses = self.helper.getMailAddresses()
        filteredAdrresses = []

        # loop ueber alle bereits vorhandenen Mail Adressen
        for mail in mailAddresses:
            # Wenn ein teilstueck der eingabe in der Mailadresse vorhanden wird die Adresse in das Array der gefilterten adressen hinzugefuegt
            if text in mail:
                filteredAdrresses.append(mail)

        # loescht die Auswahlliste der Emails
        self.ids.grid.clear_widgets()

        # wenn gefilterte Adressen vorhanden
        if filteredAdrresses:
            # loop ueber gefilterte Adressen um diese zur Auswahl in Scrollview anzuzeigen
            for address in filteredAdrresses:
                button = Button(text=address, size_hint_y=None, height=40, font_size=16)
                button.bind(on_press=partial(self.setTextInput, address))
                self.ids.grid.add_widget(button)


    # Wird aufgerufen sobald auf "Senden" gedrueckt wird
    def sendEmail(self, mailAddress):

        # Textfeld mit Emailadresse wieder leeren
        self.ids.emailInput.text = ""

        # prueft ob Emailadresse bereits gespeichert ist, falls nein speichern
        if self.helper.findMailAddressByMail(mailAddress) == None:
            self.helper.addMailAddress(mailAddress)

        mailtext = self.helper.getMailText()

        # Email im Hintergrund verschicken
        mail_thread = threading.Thread(target=self.mail.send, args=(mailAddress,mailtext))
        mail_thread.start()

        # Wieder zum Startbildschirm zuruek navigieren
        self.parent.current = 'MenuScreen'

    # Wird aufgerufen wenn Benutzer auf eine Emailadresse aus der Vorschlagsliste klickt
    # schreibt die Auswahl in das Textfeld
    def setTextInput(self, address, *args):
        self.ids.emailInput.text = address
    
    
    # @mainthread
    # def on_enter(self):

    #     mailAddresses = self.helper.getMailAddresses()

    #     self.ids.grid.clear_widgets()

    #     for address in mailAddresses:
    #         button = Button(text=address, size_hint_y=None, height=40, font_size=16)
    #         button.bind(on_press=partial(self.setTextInput, address))
    #         self.ids.grid.add_widget(button)

class FotoPopup(Popup):
    pass

class FotoImage(Image):
    pass

class FotoScreen(Screen):


    def on_enter(self):

        app = App.get_running_app()

        taskLong = app.TASK_LONG if app.TASK_LONG != None else ""
        taskShort = app.TASK_SHORT
        app.TASK_LONG = None            
        app.TASK_SHORT = None
        fromtakefoto = app.FROMTAKEFOTO
        counter = 0
        
        if fromtakefoto:
            #self.ids.FotoImageID.source='img/loading.gif'
            app.FROMTAKEFOTO = False
            isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()
            while (isResizeInprogress and counter < 15):
                print(counter)
                print(isResizeInprogress)
                counter += 1
                sleep(0.5)
                isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()

            print('afterwhile')
            thumbnailimage = app.SM.get_screen('TakeFotoScreen').res.getName()
            print(thumbnailimage)
            self.ids.FotoImageID.source='img/loading.gif'
            #self.ids.FotoImageID.source=thumbnailimage

        labeltext = "Deine Aufgabe lautet: " + taskLong if taskLong != "" else "" 
        self.ids.FotoTaskLabel.text = labeltext

    # def doFoto(self, task=None):
    #     camera = Camera()
    #     # res = ImageResize()
    #     helper = Helper()

    #     print("DoFoto called")

    #     # def open_video(self):
    #     fotoPopup = FotoPopup()
    #     self.ids.FotoScreenContainer.add_widget(fotoPopup)
            # self.camera.start()
    


class VideoScreen(Screen):
    pass

class TakeFotoScreen(Screen):
    camera = Camera()
    res = ImageResize()
    helper = Helper()
    resize_thread = None
    
    def ThreadCheck(self):
        return self.resize_thread.isAlive()
    
    def on_enter(self):
        self.camera.start()
        app = App.get_running_app()
        app.IMAGENAME = self.camera.getName()
        imgname = self.camera.getName()
        # Email im Hintergrund verschicken
        self.resize_thread = threading.Thread(name='resize_deamon', target=self.res.imgresize, args=(self.camera.getName(),))
        self.resize_thread.start()
##        self.ThreadCheck()
##        sleep(10)
##        self.ThreadCheck()
        app.FROMTAKEFOTO = True
        self.parent.current = 'FotoScreen'
        

class SuccessButton(Button):
    pass

class BackHomeButton(Button):
    pass

class InnerBoxLayout(BoxLayout):
    pass

class TaskLabel(Label):
    pass

class TaskScreen(Screen):
    
    helper = Helper()

    def on_enter(self):
        print("TaskScreen entered")

        self.ids.taskRootScreen.clear_widgets()

        task = self.helper.getRandomTask()

        boxLayout = InnerBoxLayout(
            orientation = 'horizontal'
        )

        label = Label(
            text = "Deine Aufgabe lautet:",
            size_hint_y = None,
            height = self.parent.height * 0.1,
            pos=(100, 100),
            font_size=20
        )

        labelTask = TaskLabel(
            text=task["long"],
            font_size=32
        )

        startTaskButton = SuccessButton(text="LOS!")
        startTaskButton.bind(on_press=partial(self.startTask, task["long"], task["short"]))
        
        boxLayout.add_widget(labelTask)
        boxLayout.add_widget(startTaskButton)
        self.ids.taskRootScreen.add_widget(label)
        self.ids.taskRootScreen.add_widget(boxLayout)

        self.ids.taskRootScreen.add_widget(BackHomeButton())


    def startTask(self, taskLong, taskShort, *args):
        app = App.get_running_app()
        app.TASK_SHORT = taskShort
        app.TASK_LONG = taskLong
        self.parent.current = 'FotoScreen'


class ScreenManagement(ScreenManager):
    pass

# kv Datei laden
screenmanager = Builder.load_file("./templates/ScreenManager.kv")

class ScreenManagerApp(App):

    TASK_SHORT = None
    TASK_LONG = None
    FROMTAKEFOTO = False
    SM = screenmanager

    def build(self):
        return screenmanager

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()
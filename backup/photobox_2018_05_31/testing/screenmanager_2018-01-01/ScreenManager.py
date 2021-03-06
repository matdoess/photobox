from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread

from functools import partial

from Helper import Helper
from SendEmail import SendEmail

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



class FotoScreen(Screen):


    def on_enter(self):

        app = App.get_running_app()

        taskLong = app.TASK_LONG if app.TASK_LONG != None else ""
        taskShort = app.TASK_SHORT
        app.TASK_LONG = None            
        app.TASK_SHORT = None

        labeltext = "Deine Aufgabe lautet: " + taskLong if taskLong != "" else "" 
        self.ids.FotoTaskLabel.text = labeltext


class VideoScreen(Screen):
    pass

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
presentation = Builder.load_file("./templates/ScreenManager.kv")

class ScreenManagerApp(App):

    TASK_SHORT = None
    TASK_LONG = None

    def build(self):
        return presentation

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()
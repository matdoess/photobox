import configparser

config = configparser.ConfigParser()
config.read('./config/global-config.ini')

private_config = configparser.ConfigParser()
private_config.read('./config/private-config.ini')

from kivy.config import Config
Config.read(config['kivy']['config_file'])

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import mainthread
from kivy.core.window import Window #Für Keyboard Shortscuts

#
from kivy.uix.vkeyboard import VKeyboard
VKeyboard.layout_path = config['keyboard']['layout_path']
VKeyboard.layout = config['keyboard']['layout']

#import os
#os.environ["KIVY_IMAGE"]="pil"

from os import access, R_OK
from os.path import isfile

from functools import partial
from time import sleep

from Helper import Helper
from SendEmail import SendEmail
from Camera import Camera
from PiCam import PiCam
from ImageResize import ImageResize

import threading


# Screens definieren
class StartUpScreen(Screen):
##    def on_enter(self):
##        self.current = 'MenuScreen'
##        sleep(10)
##        app = App.get_running_app()
##        app.SM.current = 'MenuScreen'
    pass

class MenuScreen(Screen):
    def on_pre_leave(self):
        pass
        #app = App.get_running_app()
        #print('MenuScreen on_pre_leave')
        #app.TASK_LONG = None
        #app.TASK_SHORT = None
    def on_enter(self):
        app = App.get_running_app()
        app.TASK_LONG = None
        app.TASK_SHORT = None

class HelpScreen(Screen):
    def on_pre_enter(self):
        self.ids.HelpImageId.source = config['images']['help_person']
        self.ids.HelpScreenLabel.text = config['text']['help_text']

    def sending_help(self):
        self.ids.HelpScreenLabel.text = config['text']['help_sending_text']  

    def send_help(self):
        print("send_help ausgeführt")

        # Create Imagestream Objekt and Take Picture
        camera = Camera()
        camera.stream()
        # Bild wird in camera.imagestream gespeichert

        # Telegram
        import telegram
        chat_id = private_config['telegram']['help_person_id']

        #image.save(bio, 'JPEG')
        #bio.seek(0)

        print("Create BOT start")
        bot = telegram.Bot(token=private_config['telegram']['api-token'])
        print("Create BOT end")
        #print(bot.get_me())
        print("Send message start")
        bot.send_message(chat_id, text="Photobox SOS")
        print("Send image start")
        bot.send_photo(chat_id, photo=camera.imagestream)
        print("Send ENDE")

        self.ids.HelpScreenLabel.text = config['text']['help_success_text']    

class HelpSendButton(Button):
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
        
        app = App.get_running_app()
        mailimage = app.MAILIMAGE
        app.MAILIMAGE = None

        # Email im Hintergrund verschicken
        mail_thread = threading.Thread(target=self.mail.send, args=(mailAddress,mailtext,mailimage))
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

    def on_pre_enter(self):
        app = App.get_running_app()
        fromtakefoto = app.FROMTAKEFOTO
        fromtaskfoto = app.FROMTASKFOTO
        self.ids.sendEmailButton.disabled = True    
        
        if fromtaskfoto:
            app.FROMTASKFOTO = False
            self.ids.ButtonTakeFoto.text = 'Aufgabe wiederholen'
        else:
            self.ids.ButtonTakeFoto.text = 'Foto aufnehmen'

        if fromtakefoto:
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            
            label = Label(
                text = "Dein Bild wird geladen",
                font_size=20
            )
            self.ids.FotoImageContainer.add_widget(label)

        else:
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            app.MAILIMAGE = None
        
        taskshort = app.TASK_SHORT
        tasklong = app.TASK_LONG
        if tasklong and not fromtaskfoto:
            
            boxLayout = InnerBoxLayout(
                orientation = 'vertical',
                padding = 20
            )
            
            label = Label(
                text = "Deine Aufgabe lautet:",
                size_hint_y = None,
                height = self.parent.height * 0.1,
                pos=(100, 100),
                font_size=20
            )
            
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            
            tasklabel = TaskLabel(
            text = tasklong,
            font_size=32
            )

            taskstupid = Label(
            text = 'Bereit?\nKlicke auf "Foto aufnehmen"',
            font_size=20
            )
            
            boxLayout.add_widget(label)
            boxLayout.add_widget(tasklabel)
            boxLayout.add_widget(taskstupid)
            self.ids.FotoImageContainer.add_widget(boxLayout)
            print(app.TASK_SHORT)

            
    def on_enter(self):

        app = App.get_running_app()
        print(app.TASK_SHORT)
        taskLong = app.TASK_LONG if app.TASK_LONG != None else ""
        taskShort = app.TASK_SHORT
        fromtakefoto = app.FROMTAKEFOTO
        counter = 0
        
        if fromtakefoto:
##            self.ids.FotoImageID.source='img/loading_black.gif'
##            print('fromtakefotostart')
##            label = Label(
##            text = "Deine Aufgabe lautet:",
##            size_hint_y = None,
##            height = self.parent.height * 0.1,
##            pos=(100, 100),
##            font_size=20
##            )
##
##            self.ids.FotoImageContainer.add_widget(label)
            
            app.FROMTAKEFOTO = False
            isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()
            sleep(2)
            while (isResizeInprogress and counter < 15):
                print(counter)
                print(isResizeInprogress)
                counter += 1
                sleep(0.5)
                isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()

            thumbnailimage = app.SM.get_screen('TakeFotoScreen').res.getName()

            if isfile(thumbnailimage) and access(thumbnailimage, R_OK):
                self.ids.sendEmailButton.disabled = False   
                fotoimage = FotoImage(source=thumbnailimage)
            else:
                fotoimage = FotoImage(source=config['images']['error_no_photo'])

            self.ids.FotoImageContainer.clear_widgets()
            self.ids.FotoImageContainer.add_widget(fotoimage)
            app.MAILIMAGE = thumbnailimage
            
            #self.ids.FotoImageID.source='img/loading_black.gif'
            #self.ids.FotoImageID.source=thumbnailimage

        #labeltext = "Deine Aufgabe lautet: " + taskLong if taskLong != "" else "" 
        #self.ids.FotoTaskLabel.text = labeltext

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
    
    def on_pre_enter(self):
        app = App.get_running_app()
        fromtakevideo = app.FROMTAKEVIDEO
        app.FROMTAKEVIDEO = None
        if fromtakevideo:
            self.ids.VideoScreenContainer.clear_widgets()
            fotoimage = FotoImage(source='img/video_icon.png')
            self.ids.VideoScreenContainer.add_widget(fotoimage)
            
            label = TaskLabel(
            text = "Danke das du dem Brautpaar eine Nachricht hinterlassen hast.",
            font_size=20
            )
            self.ids.VideoScreenContainer.add_widget(label)
        else:
            self.ids.VideoScreenContainer.clear_widgets()
            fotoimage = FotoImage(source='img/video_icon.png')
            self.ids.VideoScreenContainer.add_widget(fotoimage)
            
            label = TaskLabel(
            text = "Hier kannst du dem Brautpaar eine Videonachricht aufnehmen.\n\nTippe auf den Bildschirm um die Aufnahme zu stoppen.",
            font_size=20
            )
            self.ids.VideoScreenContainer.add_widget(label)
            
    
##    def on_enter(self):
##        app = App.get_running_app()
##        app.show_popup('Popup aus Video datei')

class TakeFotoScreen(Screen):
    camera = Camera()
    res = ImageResize()
    helper = Helper()
    resize_thread = None
    
    def ThreadCheck(self):
        return self.resize_thread.isAlive()
    
    def on_enter(self):
        app = App.get_running_app()
        #print(app.TASK_SHORT)
        taskshort = app.TASK_SHORT if app.TASK_SHORT else ""
        tasklong = app.TASK_LONG if app.TASK_LONG else ""
        self.camera.textlong = tasklong
        self.camera.textshort = taskshort
        
        self.camera.start()
        app.IMAGENAME = self.camera.getName()
        imgname = self.camera.getName()

        # Resize Deamon
        self.resize_thread = threading.Thread(name='resize_deamon', target=self.res.imgresize, args=(self.camera.getName(),))
        self.resize_thread.start()
##        self.ThreadCheck()
##        sleep(10)
##        self.ThreadCheck()
        app.FROMTAKEFOTO = True
        app.FROMTASKFOTO = True if tasklong else False
        print("FROMTASKFOTO:")
        print(app.FROMTASKFOTO)
        self.parent.current = 'FotoScreen'
        
class TakeVideoScreen(Screen):
    
    picam = PiCam()
    
    def on_enter(self):
        self.picam.init()
        sleep(1)
        self.picam.start()
    
##    def picam_init(self):
##        self.picam.init()
    
    def picam_quit(self):
        self.picam.quit()
    
##    def picam_start(self):
##        self.picam.start()
    
    def picam_stop(self):
        self.picam.stop()
    
    def sleep(self, time):
        sleep(time)
        
    def set_fromtakevideo(self):
        app = App.get_running_app()
        app.FROMTAKEVIDEO = True

class SuccessButton(Button):
    pass


class HelpButton(Button):
    pass


class BackHomeButton(Button):
##    def clear_tasks(self):
##        app = App.get_running_app()
##        app.TASK_LONG = None
##        app.TASK_SHORT = None
    pass

class InnerBoxLayout(BoxLayout):
    pass

class TaskLabel(Label):
    pass

class TaskButton(Button):
    helper = Helper()

    def get_task(self):
        print("get_task ausgeführt")

        task = self.helper.getRandomTask()
        
        app = App.get_running_app()
        app.TASK_SHORT = task["short"]
        app.TASK_LONG = task["long"]
        #print(app.TASK_LONG)
        
        #self.parent.current = 'FotoScreen'

class ScreenManagement(ScreenManager):
    pass

# kv Datei laden
screenmanager = Builder.load_file("./templates/ScreenManager.kv")

class CustomPopup(Popup):
    pass

class PopupButton(Button):
    pass

class ScreenManagerApp(App):

    TASK_SHORT = None
    TASK_LONG = None
    FROMTAKEFOTO = False
    FROMTASKFOTO = False
    FROMTAKEVIDEO = False
    SM = screenmanager
    MAILIMAGE = None
    
    def show_popup(self, popuptext, popuptype = None):
        popupboxlayout = BoxLayout(orientation='vertical')
        popup = CustomPopup(title='Info',
                            content=popupboxlayout)
        
        popupboxlayout.add_widget(Label(text=popuptext))
        popupboxlayout.add_widget(PopupButton(text='OK', height=60, size_hint_y = None, on_press = popup.dismiss))
        
        popup.open()
        
    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        if modifier == ['ctrl'] and codepoint == 'k':
            print('stop')
            self.stop()
        if codepoint == 'k':
            self.stop()
        print('windows' + str(window) + 'key' + str(key) + 'scancode' + str(scancode) + 'codepoint' + str(codepoint) + 'modifier' + str(modifier))
        
    def build(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window._system_keyboard.keycodes['ctrl'] = 305
        return screenmanager
    
##    def on_start(self):
##        print('on_start')
##        self.current = 'MenuScreen'

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()
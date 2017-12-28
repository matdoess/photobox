from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from kivy.clock import mainthread

from functools import partial

from Helper import Helper
from SendEmail import SendEmail

from time import sleep
import threading

# kv Datei laden
Builder.load_file("./templates/ScreenManager.kv")

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
        self.parent.current = 'menu'

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
    def sleep(self, time):
        sleep(time)

class VideoScreen(Screen):
    pass

class TaskScreen(Screen):
    pass


# Screenmanager erzeugen
sm = ScreenManager(transition=WipeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FotoScreen(name='foto'))
sm.add_widget(VideoScreen(name='video'))
sm.add_widget(TaskScreen(name='task'))
sm.add_widget(SendEmailScreen(name='sendemail'))

class ScreenManagerApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()
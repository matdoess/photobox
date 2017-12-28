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

Builder.load_file("./templates/ScreenManager.kv")

# Declare screens
class MenuScreen(Screen):
    pass

class SendEmailScreen(Screen):
    helper = Helper()
    mail = SendEmail()

    def inputChanged(self, text, *args):

        mailAddresses = self.helper.getMailAddresses()
        filteredAdrresses = []

        for mail in mailAddresses:
            if text in mail:
                filteredAdrresses.append(mail)

        self.ids.grid.clear_widgets()

        if filteredAdrresses:
            for address in filteredAdrresses:
                button = Button(text=address, size_hint_y=None, height=40, font_size=16)
                button.bind(on_press=partial(self.setTextInput, address))
                self.ids.grid.add_widget(button)

    def sendEmail(self, mailAddress):

        self.ids.emailInput.text = ""

        if self.helper.findMailAddressByMail(mailAddress) == None:
            self.helper.addMailAddress(mailAddress)

        mailtext = self.helper.getMailText()

        mail_thread = threading.Thread(target=self.mail.send, args=(mailAddress,mailtext))
        mail_thread.start()

        self.parent.current = 'menu'

    # @mainthread
    # def on_enter(self):

    #     mailAddresses = self.helper.getMailAddresses()

    #     self.ids.grid.clear_widgets()

    #     for address in mailAddresses:
    #         button = Button(text=address, size_hint_y=None, height=40, font_size=16)
    #         button.bind(on_press=partial(self.setTextInput, address))
    #         self.ids.grid.add_widget(button)


    def setTextInput(self, address, *args):
        self.ids.emailInput.text = address

class FotoScreen(Screen):
    def sleep(self, time):
        sleep(time)

class VideoScreen(Screen):
    pass

class TaskScreen(Screen):
    pass


# Create the screen manager
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
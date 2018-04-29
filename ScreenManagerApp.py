import settings

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from kivy.core.window import Window #Für Keyboard Shortscuts

from kivy.uix.vkeyboard import VKeyboard
VKeyboard.layout_path = settings.myList['config']['keyboard']['layout_path']
VKeyboard.layout = settings.myList['config']['keyboard']['layout']

import threading

from Helper import Helper

# Screens definieren
from screens import StartUpScreen

from screens import MenuScreen

from screens import HelpScreen

from screens import SendEmailScreen

from screens import FotoScreen

from screens import VideoScreen

from screens import TakeFotoScreen

from screens import TakeVideoScreen

class HelpSendButton(Button):
    pass

class SuccessButton(Button):
    pass


class HelpButton(Button):
    pass


class BackHomeButton(Button):
    pass

class PopupButton(Button):
    pass

class TaskButton(Button):
    helper = Helper()

    def get_task(self):
        task = self.helper.getRandomTask()
        
        app = App.get_running_app()
        app.TASK_SHORT = task["short"]
        app.TASK_LONG = task["long"]

class ScreenManagement(ScreenManager):
    pass

# kv Datei laden
screenmanager = Builder.load_file("./templates/screenManager.kv")

class ScreenManagerApp(App):

    TASK_SHORT = None
    TASK_LONG = None
    FROMTAKEFOTO = False
    FROMTASKFOTO = False
    FROMTAKEVIDEO = False
    SM = screenmanager
    MAILIMAGE = None
        
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
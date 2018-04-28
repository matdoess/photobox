import settings

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

from kivy.uix.vkeyboard import VKeyboard
VKeyboard.layout_path = settings.myList['config']['keyboard']['layout_path']
VKeyboard.layout = settings.myList['config']['keyboard']['layout']

from os import access, R_OK
from os.path import isfile

from functools import partial
from time import sleep

from Helper import Helper
from Camera import Camera
from PiCam import PiCam
from ImageResize import ImageResize

import threading

# Screens definieren
from screens import StartUpScreen

from screens import MenuScreen

from screens import HelpScreen

from screens import SendEmailScreen

from screens import FotoScreen

from screens import VideoScreen

class HelpSendButton(Button):
    pass

class FotoPopup(Popup):
    pass

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
    
    def picam_quit(self):
        self.picam.quit()

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
    pass

class InnerBoxLayout(BoxLayout):
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
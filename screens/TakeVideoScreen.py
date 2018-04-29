from kivy.uix.screenmanager import Screen
from kivy.app import App

from time import sleep

from PiCam import PiCam

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
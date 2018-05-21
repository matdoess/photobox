from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import Clock
from functools import partial

from time import sleep

from PiCam import PiCam

import settings

class TakeVideoScreen(Screen):
    
    picam = PiCam()

    def on_enter(self):
        self.countdown3 = Clock.schedule_once(partial(self.countdown, '3'), 0)
        self.countdown2 = Clock.schedule_once(partial(self.countdown, '2'), 1)
        self.countdown1 = Clock.schedule_once(partial(self.countdown, '1'), 2)
        self.start_video_event = Clock.schedule_once(lambda dt: self.start_video(), 3)

    def countdown(self, number, *dt):
        self.ids.TakeVideoBackgroundButton.text = number

    def start_video(self):
        self.countdown(number="")
        self.picam.init()
        sleep(1)
        self.picam.start()
        self.schedule_quit_video()
    
    def picam_quit(self):
        self.picam.quit()

    def picam_stop(self):
        self.picam.stop()
    
    def sleep(self, time):
        sleep(time)
        
    def set_fromtakevideo(self):
        app = App.get_running_app()
        app.FROMTAKEVIDEO = True

    def quit_video(self):
        print('quit_video() executed')
        self.quit_video_event.cancel()
        self.set_fromtakevideo()
        self.picam_stop()
        self.sleep(1)
        self.picam_quit()
        self.parent.current = 'VideoScreen'

    def quit_video_callback(self,dt):
        print('quit_video_callback() executed')
        self.quit_video()
    
    #quit_video_event = Clock.create_trigger(quit_video_callback, 5)

    def schedule_quit_video(self):
        print('schedule_quit_video() executed')
        #self.quit_video_event()
        self.quit_video_event = Clock.schedule_once(self.quit_video_callback, float(settings.myList['config']['video']['timeout']))

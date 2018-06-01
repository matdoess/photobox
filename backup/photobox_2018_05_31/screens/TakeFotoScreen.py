from kivy.uix.screenmanager import Screen
from kivy.app import App

from Camera import Camera
from Helper import Helper
from ImageResize import ImageResize

import threading


class TakeFotoScreen(Screen):
    camera = Camera()
    res = ImageResize()
    helper = Helper()
    resize_thread = None
    
    def ThreadCheck(self):
        return self.resize_thread.isAlive()
    
    def on_enter(self):
        app = App.get_running_app()
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
        self.parent.current = 'FotoScreen'
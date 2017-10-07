# Kivy
import kivy
from kivy.app import App
##from kivy.uix.button import Button
##from kivy.uix.scatter import Scatter
##from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label
from kivy.uix.popup import Popup

#PiCamera
from picamera import PiCamera

#Sonstige
from time import sleep
from datetime import datetime
#################################################################

class CustomPopup(Popup):
    
    global imagename
    def imagename():
        imagepath = 'pics/'
        imagedatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        imagesuffix = '_Test'
        imageext = '.jpg'
        imagenamecomplete = imagepath + imagedatetime + imagesuffix + imageext
        return imagenamecomplete
    
    # Camera
    def video(self):
        camera = PiCamera()

        camera.rotation = 180
        camera.resolution = (3280, 2464)
        #camera.resolution = (2000, 2000)
        #camera.framerate = 15

        camera.start_preview(resolution=(1640, 1232))
        sleep(5)
        camera.annotate_text = 'Hello world!'
        camera.capture(imagename())
        camera.stop_preview()

class HomeGridLayout(GridLayout):
    
    # Camera
    def video(self):
        camera = PiCamera()

        camera.rotation = 180
        camera.resolution = (3280, 2464)
        #camera.resolution = (2000, 2000)
        #camera.framerate = 15

        camera.start_preview(resolution=(1640, 1232))
        sleep(5)
        camera.annotate_text = 'Hello world!'
        camera.capture('pics/image6.jpg')
        camera.stop_preview()
        
    # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class PhotoboxApp(App):
    
    def build(self):
        return HomeGridLayout()

Photobox = PhotoboxApp()

Photobox.run()
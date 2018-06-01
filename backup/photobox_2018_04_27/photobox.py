# Kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup


#Sonstige
from time import sleep
from datetime import datetime
import random
import sys
import threading

#Eigene Module
from Helper import Helper
from SendEmail import SendEmail
from PiCam import PiCam
from ImageResize import ImageResize
from Camera import Camera

import os
host = os.environ.get('HOSTNAME')

if host == "raspberrypi":
    #PiCamera
    from picamera import PiCamera


#################################################################

### FUNCTIONS ###

# Imagename erstellen
##global imagename
##def imagename():
##    imagepath = 'pics/'
##    imagedatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
##    imagesuffix = '_Test'
##    imageext = '.jpg'
##    imagenamecomplete = imagepath + imagedatetime + imagesuffix + imageext
##    return imagenamecomplete

# Camera
##global video
##def video():
##    print("Picamera Function");
##    if host == "raspberrypi":
##        camera = PiCamera()
##        
##        camera.rotation = 180
##        camera.resolution = (3280, 2464)
##        #camera.resolution = (2000, 2000)
##        #camera.framerate = 15
##        camera.start_preview(resolution=(1640, 1232), fullscreen=False, window=(0,0,800,480))
##        sleep(5)
##        camera.annotate_text = 'Hello world!'
##        camera.capture(imagename())
##        camera.stop_preview()
##        camera.close()
        
### KIVY ###

class CustomPopup(Popup):
    camera = Camera()
    res = ImageResize()
    helper = Helper()
    def open_video(self):
        self.camera.start()
        #print('Bild wurde gespeichert:' + camera.getname())
    def img_resize(self):
        self.res.imgresize(self.camera.getName())
        print('Komprimiertes Bild gespeichert unter:' + self.res.getName())
    def send_email(self):
        mail = SendEmail()
        receiver='jody1990.jl@gmail.com'
        mailtext = self.helper.getMailText()
        mailfile = self.res.getName()
        #mail.send(receiver,mailtext) #Backgroundprozess
        mail_thread = threading.Thread(target=mail.send, args=(receiver,mailtext,mailfile))
        mail_thread.start()

class VideoPopup(Popup):

    picam = PiCam()
    
    def picam_init(self):
        self.picam.init()
    
    def picam_quit(self):
        self.picam.quit()
    
    def picam_start(self):
        self.picam.start()
    
    def picam_stop(self):
        self.picam.stop()
    
    def sleep(self, time):
        sleep(time)

        
class TaskPopup(Popup):
    
    helper = Helper()

    def randomtask(self):
        tasks = self.helper.getTasks();
        taskButtonText = random.choice(list(tasks.keys()))

        tasktextbutton1 = self.ids['tasktextbutton']
        tasktextbutton1.text = taskButtonText

    def sendEmail(self):

        mailtext = self.helper.getMailText()
        receiver = "jody.lerch@web.de"
        # receiver = "matthiasdoess@gmail.com"

        mail = SendEmail()
        mail.send(receiver, mailtext);
    

class HomeGridLayout(GridLayout):
    
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        
    def open_videopopup(self):
        the_videopopup = VideoPopup()
        the_videopopup.open()
        # sys.exit("Error message")
        
    def open_taskpopup(self):
        the_taskpopup = TaskPopup()
        the_taskpopup.open()

class PhotoboxApp(App):
    
    def build(self):
        return HomeGridLayout()

Photobox = PhotoboxApp()

Photobox.run()
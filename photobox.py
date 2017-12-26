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

#Process Management
import shlex
from subprocess import Popen
from subprocess import run

#Sonstige
from time import sleep
from datetime import datetime
import random
#################################################################

### FUNCTIONS ###

# Aufgabenliste
global taskdict
global taskshort
global tasklong
taskdict = {'kuss':'Küsst euch',
            'grimasse':'Schneide eine Grimasse',
            'model':'Mach eine Modelpose',
            'herz':'Mach ein Herz mit der Hand',
            'profil':'Lass ein Profil fotografieren',
            'prost':'Stoße mit jemandem an'}
#taskshort = random.choice(list(taskdict.keys()))
#tasklong = taskdict[taskshort]

# Imagename erstellen
global imagename
def imagename():
    imagepath = 'pics/'
    imagedatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    imagesuffix = '_Test'
    imageext = '.jpg'
    imagenamecomplete = imagepath + imagedatetime + imagesuffix + imageext
    return imagenamecomplete

# Camera
global video
def video():
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
    camera.close()

# picam
global picam
def picam(input):
    if input is 'init':
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
        
    elif input is 'quit':
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)
    
    elif input is 'start':
        pscmd = shlex.split("touch /home/pi/picam/hooks/start_record")
        run(pscmd)
    
    elif input is 'stop':
        pscmd = shlex.split("touch /home/pi/picam/hooks/stop_record")
        run(pscmd)
        
    else:
        print("wrong input")
        
### Eigene Classen ###
    
class StorageClass():
    selection = ""
    def setselection(self,value):
        self.selection = value
    def getselection(self):
        return self.selection

### Eigene Objekte ###
global storage
storage = StorageClass()
        
### KIVY ###

class CustomPopup(Popup):
    
    def open_video(self):
        video()

class VideoPopup(Popup):
    
    def picam_init(self):
        picam('init')
    def picam_quit(self):
        picam('quit')
    def picam_start(self):
        picam('start')
    def picam_stop(self):
        picam('stop')
    def sleep(self, time):
        sleep(time)
        
class TaskPopup(Popup):
    
##    taskshort = "foobar"
    def randomtask(self):
        foobar = random.choice(list(taskdict.keys()))
##        self.taskshort =
##        print('randomtask called' + self.taskshort)
##        return random.choice(list(taskdict.keys()))
        tasktextbutton1 = self.ids['tasktextbutton']
        tasktextbutton1.text = foobar
        storage.setselection(foobar)
        print(storage.getselection())
    

class HomeGridLayout(GridLayout):
    
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        
    def open_videopopup(self):
        the_videopopup = VideoPopup()
        the_videopopup.open()
        
    def open_taskpopup(self):
        the_taskpopup = TaskPopup()
        the_taskpopup.open()

class PhotoboxApp(App):
    
    def build(self):
        return HomeGridLayout()

Photobox = PhotoboxApp()

Photobox.run()
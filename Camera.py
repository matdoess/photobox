from PIL import Image
from time import sleep
from imagename import imagename

import os
host = os.environ.get('HOSTNAME')

if host == "raspberrypi":
    #PiCamera
    from picamera import PiCamera
    
class Camera():
    imgname = ""
    
    def start(self):
        print("Picamera Function");
        if host == "raspberrypi":
            cam = PiCamera()
            
            cam.rotation = 180
            cam.resolution = (3280, 2464)
            #camera.resolution = (2000, 2000)
            #camera.framerate = 15
            
            cam.start_preview(resolution=(1640, 1232), fullscreen=False, window=(0,0,800,480))
            sleep(5)
            cam.annotate_text = 'Hello world!'
            self.imgname = imagename()
            cam.capture(self.imgname)
            cam.stop_preview()
            cam.close()
            
    def getName(self):
        return self.imgname
#
# TEST
#
##print(imagename())
##camera = Camera()
##camera.start()
##print(camera.getname())

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
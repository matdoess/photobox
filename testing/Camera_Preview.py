from PIL import Image
from time import sleep
import imagename

import os
#host = os.environ.get('HOSTNAME')
host = 'raspberrypi'
print('host= ' + host)

if host == "raspberrypi":
    #PiCamera
    from picamera import PiCamera
    
class Camera():
    
    # Settings
    mirror = False
    
    # Load images
    img3 = Image.open('img/3.png')
    img2 = Image.open('img/2.png')
    img1 = Image.open('img/1.png')
    images = [img3,img2,img1]
    imgwhite = Image.open('img/white.png')
    
    #Variablen
    imgname = ""
    textshort = ""
    textlong = ""
    textsize = 64
    
    def start(self):
        print("Picamera Function");
        if host == "raspberrypi":
            cam = PiCamera()
            
            cam.vflip = True
            cam.resolution = (3280, 2464)
            #cam.resolution = (2000, 2000)
            #cam.framerate = 15
            
            cam.start_preview(resolution=(1640, 1232), fullscreen=False, window=(0,0,800,480))
            #sleep(5)
            
            # Add Overlay Countdown For-Schleife
            sleep(1)
            for i in self.images:
                o = cam.add_overlay(i.tobytes(), size=i.size, layer=3)
                sleep(1)
                cam.remove_overlay(o)
            #Flash White
            sleep(120)    
            o = cam.add_overlay(self.imgwhite.tobytes(), size=self.imgwhite.size, layer=3)
            o.alpha=128
            sleep(0.2)
            
            #cam.remove_overlay(o)
            cam.annotate_text_size = self.textsize
            cam.annotate_text = self.textlong
            self.imgname = imagename(self.textshort)
            #print(self.imgname)
            if self.mirror:
                cam.hflip = True
            cam.capture(self.imgname)
            if self.mirror:
                cam.hflip = False
            cam.stop_preview()
            cam.close()
            
            
    def getName(self):
        return self.imgname
#
# TEST
#
if __name__ == "__main__":
    print(imagename())
    camera = Camera()
    camera.textshort = 'kuss'
    camera.textlong = 'Hochzeit von Elisabeth & Johannes' 
    camera.start()
    print(camera.getName())

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
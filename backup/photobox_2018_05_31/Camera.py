from PIL import Image
from io import BytesIO
from time import sleep

#Randomimage
import random
from shutil import copyfile
from os import listdir
from os.path import isfile, join
#

from Helper import Helper

import settings

if settings.myList["env"] == "raspberrypi":
    #PiCamera
    from picamera import PiCamera
    
class Camera():
    import configparser
    config = configparser.ConfigParser()
    config.read('./config/global-config.ini')

    # Settings
    mirrorview = config['camera'].getboolean('mirrorview')
    mirror = config['camera'].getboolean('mirror')
    # Flashmode on,auto,off,redeye,fillin,torch
    flashmode = settings.myList['config']['camera']['flashmode']
    upsidedown = config['camera'].getboolean('upsidedown')
    
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

    #Objekte
    imagestream = BytesIO()
    imagestream.name = ""

    
    def start(self):
        
        helper = Helper()

        if settings.myList["env"] == "raspberrypi":
            cam = PiCamera()
            
            cam.flash_mode = self.flashmode
            cam.vflip = self.upsidedown
            cam.hflip = self.mirrorview
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
            o = cam.add_overlay(self.imgwhite.tobytes(), size=self.imgwhite.size, layer=3)
            o.alpha=128
            sleep(0.2)
            
            #cam.remove_overlay(o)
            cam.annotate_text_size = self.textsize
            cam.annotate_text = self.textlong
            self.imgname = helper.getImagename(self.textshort)
            #print(self.imgname)
            if self.mirror:
                cam.hflip = not cam.hflip
            cam.capture(self.imgname)
            if self.mirror:
                cam.hflip = not cam.hflip
            cam.stop_preview()
            cam.close()
        else:
            self.imgname = helper.getImagename('random')
            randomimage = self.getRandomImage()
            copyfile(randomimage,self.imgname)
            print(self.imgname)
             
    def getName(self):
        return self.imgname

    def stream(self):
        print("Picamera Image Stream to ByteIO Objekt")
        if settings.myList['env'] == "raspberrypi":
            cam = PiCamera()
            
            cam.vflip = self.upsidedown
            cam.hflip = self.mirrorview
            cam.resolution = (640, 480)
            
            cam.start_preview()
            cam.preview.alpha = 0
            sleep(2)
            
            if self.mirror:
                cam.hflip = not cam.hflip
            cam.capture(self.imagestream, 'jpeg')
            if self.mirror:
                cam.hflip = not cam.hflip
            cam.stop_preview()
            cam.close()

            self.imagestream.seek(0)
            print("Camera.imagestream bereit")
        else:
            randomimage = self.getRandomImage()
            # Alter Code Funktioniert auch aber Bild wird nicht aktualisiert
            #pil_img = Image.open(randomimage)
            #pil_img.save(self.imagestream, 'jpeg')
            #pil_img.close()
            self.imagestream = open(randomimage, "rb")
            self.imagestream.seek(0)

    def getRandomImage(self):
        random_image_path = 'img/random/'

        ##Neue Methode (Auswahl aus allen Dateien im random_image_path):
        image_files = [f for f in listdir(random_image_path) if isfile(join(random_image_path, f))]
        print(image_files)
        random_image = random_image_path + random.choice(image_files)

        ## Alte Methode (Feste Dateinamen):
        # numbers = [1,2,3,4,5,6,7,8,9,10]
        # random_number = random.choice(numbers)
        # random_image = random_image_path + str(random_number) + '.jpg'
        
        print('getRandomImage')
        print(random_image)
        return random_image

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
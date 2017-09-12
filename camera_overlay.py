import picamera
from PIL import Image
from time import sleep

# Load images
img3 = Image.open('img/3.png')
img2 = Image.open('img/2.png')
img1 = Image.open('img/1.png')
imgwhite = Image.open('img/white.png')

with picamera.PiCamera() as camera:
    camera.resolution = (800, 480)
    camera.framerate = 24
    camera.start_preview()

    # Add Overlay Countdown
    sleep(1)
    #3
    o = camera.add_overlay(img3.tobytes(), size=img3.size, layer=3)
    sleep(1)
    camera.remove_overlay(o)
    #2
    o = camera.add_overlay(img2.tobytes(), size=img2.size, layer=3)
    sleep(1)
    camera.remove_overlay(o)
    #1
    o = camera.add_overlay(img1.tobytes(), size=img1.size, layer=3)
    sleep(1)
    camera.remove_overlay(o)
    #Flash White
    o = camera.add_overlay(imgwhite.tobytes(), size=imgwhite.size, layer=3)
    o.alpha=128
    sleep(0.2)
##    camera.remove_overlay(o)
    #Cheese
    camera.capture('pics/countdown.jpg')
    camera.stop_preview()

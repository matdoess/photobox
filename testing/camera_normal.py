from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (3280, 2464)
#camera.resolution = (2000, 2000)
#camera.framerate = 15

#camera.start_preview(resolution=(1640, 1232), fullscreen=False, window=(0,0,800,400))
camera.start_preview(resolution=(1640, 1232))
sleep(5)
camera.annotate_text = 'Hello world!'
camera.capture('pics/image6.jpg')
camera.stop_preview()

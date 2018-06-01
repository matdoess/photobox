import time
import picamera

with picamera.PiCamera() as camera:
    camera.flash_mode = 'on'
    camera.awb_mode = 'auto'
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Desktop/flash7on.jpg')
    camera.stop_preview()

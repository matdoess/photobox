import RPi.GPIO as GPIO

import time
import picamera

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Desktop/test1.jpg')
    camera.stop_preview()

GPIO.output(4, GPIO.LOW)
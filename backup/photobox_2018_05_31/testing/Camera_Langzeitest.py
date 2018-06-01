from Camera import Camera
from PiCam import PiCam
from ImageResize import ImageResize

counter = 0
while counter < 1000:
    print(counter)
    counter += 1
    #sleep(0.5)
    #print(imagename())
    camera = Camera()
    camera.textshort = 'test'
    camera.textlong = 'Test' 
    camera.start()
    print(camera.getName())

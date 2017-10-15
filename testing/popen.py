import shlex
from subprocess import Popen
from subprocess import run
from time import sleep

### Versuch Popen TEST ###

##def popenfunct(input):
##    if input is 'start':
##        pscmd = shlex.split("touch popen.test")
##        ps = Popen(pscmd)
##    elif input is 'stop':
##        pscmd = shlex.split("rm popen.test")
##        ps = Popen(pscmd)
##    else:
##        print("wrong input")
    
##popenfunct('start')

### Versuch Popen picam ###

##global ps
##global pscmd
##def popenfunct(input):
##    if input is 'start':
##        pscmd = shlex.split("/home/pi/picam/picam --alsadev hw:1,0 --rotation 180 --hflip --preview --previewrect 0,0,800,480")
##        ps = Popen(pscmd)
##        
##    elif input is 'stop':
####        pscmd = shlex.split("rm popen.test")
####        ps = Popen(pscmd)
##        ps.kill()
##        
##    else:
##        print("wrong input")
        
        
##popenfunct('start')



def popenfunct(input):
    if input is 'start':
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
        
    elif input is 'stop':
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)
        
    else:
        print("wrong input")
        
        
popenfunct('start')

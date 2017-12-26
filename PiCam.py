import shlex
from subprocess import Popen
from subprocess import run

class PiCam():

    def init(self):
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
        
    def quit(self):
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)
    
    def start(self):
        pscmd = shlex.split("touch /home/pi/picam/hooks/start_record")
        run(pscmd)
    
    def stop(self):
        pscmd = shlex.split("touch /home/pi/picam/hooks/stop_record")
        run(pscmd)
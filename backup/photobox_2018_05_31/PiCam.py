import os
import shlex
from subprocess import Popen
from subprocess import run
from time import sleep

from Helper import Helper
from VideoConvert import VideoConvert


class PiCam():
    #Objekte
    videoconvert = VideoConvert()

    #Variablen
    videoname = ""

    def init(self):
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
        
    def quit(self):
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)
    
    # ## start alt mit Standarddateinamen
    # def start(self):
    #     pscmd = shlex.split("touch /home/pi/picam/hooks/start_record")
    #     run(pscmd)
    #     #sleep(2)
    #     #pscmd = shlex.split("cat /home/pi/photobox/picam_config/rec.sub > home/pi/picam/hooks/subtitle")
    #     #run(pscmd)

    ## start() mit getVideoname()
    def start(self):

        helper = Helper()
        self.videoname = helper.getVideoname()
        videobasename = os.path.basename(self.videoname)
        starthook = open("/home/pi/picam/hooks/start_record", "w")

        pscmd = shlex.split("touch /home/pi/picam/hooks/start_record")
        print(pscmd)

        #Beispielstartbefehl mit Vorgabe Dateinamen
        #echo -e "filename=test0815.ts" > hooks/start_record
        startcmd = 'echo -e "filename=' + videobasename + '"'
        print(startcmd)
        pscmd = shlex.split(startcmd)
        print(pscmd)
        #run(pscmd)
        run(pscmd, stdout=starthook)
        #f = open("blah.txt", "w")
        #subprocess.call(["/home/myuser/run.sh", "/tmp/ad_xml",  "/tmp/video_xml"], stdout=f)
    

    # ## stop() alt ohne videoconvert
    # def stop(self):
    #     pscmd = shlex.split("touch /home/pi/picam/hooks/stop_record")
    #     run(pscmd)

    ## stop() mit VideoConvert()
    def stop(self):
        pscmd = shlex.split("touch /home/pi/picam/hooks/stop_record")
        run(pscmd)
        self.videoconvert.convert(self.videoname)
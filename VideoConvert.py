import os
import shlex
from subprocess import Popen
from subprocess import run

class VideoConvert():
    #
    # Settings
    #

    # Size of smaller Image side
    #imgsize='1500^>'
    #imgquality=80
    #imgaddname = '_mail'
    videoaddfolder = 'mp4'
    videonewname = ""
    videonewext = ".mp4"

    def convert(self,videofile):

        # Create Variables
        videonameext = os.path.basename(videofile)
        videoname = os.path.splitext(videonameext)[0]
        print("videoname:" + videoname)
        videoext = os.path.splitext(videofile)[1]
        print("videoext:" + videoext)
        videofolder = os.path.dirname(videofile)
        print("videofolder:" + videofolder)
        self.videonewname = videofolder + '/' + self.videoaddfolder + '/' + videoname + self.videonewext
        print(self.videonewname)

        # Check if Videofolder exists, if not create it
        checkfolder = videofolder + '/' + self.videoaddfolder
        if not os.path.exists(checkfolder):
            os.makedirs(checkfolder)
        
        # Convert Video
        pscmd = shlex.split("ffmpeg -i " + videofile +" -c:v copy -c:a copy -bsf:a aac_adtstoasc " + self.videonewname)
        print(pscmd)
        #run(pscmd)
        Popen(pscmd)

    def getName(self):
        return self.videonewname

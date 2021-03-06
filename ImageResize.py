from wand.image import Image
import os

class ImageResize():
    #
    # Settings
    #

    # Size of smaller Image side
    imgsize='1500^>'
    imgquality=80
    imgaddname = '_mail'
    imgaddfolder = 'mail'
    imgnewname = ""

    def imgresize(self,imgfile):
        
        # Create Variables
        imgnameext = os.path.basename(imgfile)
        imgname = os.path.splitext(imgnameext)[0]
        imgext = os.path.splitext(imgnameext)[1]
        imgfolder = os.path.dirname(imgfile)
        self.imgnewname = imgfolder + '/' + self.imgaddfolder + '/' + imgname + self.imgaddname + imgext
        
        # Check if Imagefolder exists, if not create it
        checkfolder = imgfolder + '/' + self.imgaddfolder
        if not os.path.exists(checkfolder):
            os.makedirs(checkfolder)
        
        # Convert Image
        with Image(filename=imgfile) as img:
            with img.clone() as converted:
                converted.transform(resize=self.imgsize)
                converted.compression_quality = self.imgquality
                converted.save(filename=self.imgnewname)

    def getName(self):
        return self.imgnewname

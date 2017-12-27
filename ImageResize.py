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
        imgnameext = os.path.basename(imgfile)
        #print('imgnameext=' + imgnameext)
        imgname = os.path.splitext(imgnameext)[0]
        #print('imgname=' + imgname)
        imgext = os.path.splitext(imgnameext)[1]
        #print('imgext=' + imgext)
        imgfolder = os.path.dirname(imgfile)
        #print('imgfolder=' + imgfolder)
        self.imgnewname = imgfolder + '/' + self.imgaddfolder + '/' + imgname + self.imgaddname + imgext
        print(self.imgnewname)
        with Image(filename=imgfile) as img:
            with img.clone() as converted:
                converted.transform(resize=self.imgsize)
                converted.compression_quality = self.imgquality
                converted.save(filename=self.imgnewname)

    def getName(self):
        return self.imgnewname

#
# TEST
#

#resize = ImageResize()
#resize.imgresize('testing/wand_imagemagick/test.jpg')

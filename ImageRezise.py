from wand.image import Image


class ImageResize():
    #
    # Settings
    #

    # Size of smaller Image side
    imgsize='1500^>'
    imgquality=80
    imgaddname = '_mail'

    def imgresize(self,imgfile):
        imgname = imgfile.split(".jpg")[0]
        imgnewname = imgname + self.imgaddname + '.jpg'
        print(imgname)
        print(imgnewname)
        with Image(filename=imgfile) as img:
            with img.clone() as converted:
                converted.transform(resize=self.imgsize)
                converted.compression_quality = self.imgquality
                converted.save(filename=self.imgnewname)


#
# TEST
#

resize = ImageResize()
resize.imgresize('testing/wand_imagemagick/test.jpg')



##with Image(filename='test.jpg') as original:
##    with original.convert('png') as converted:
##        pass
    
##with Image(filename='test.jpg') as img:
##    print('width =', img.width)
##    print('height =', img.height)

# with Image(filename='test.jpg') as original:
#     with original.clone() as converted:
#         converted.transform(resize='1500^>')
#         #converted.sample(1500,2000)
#         converted.compression_quality = 80
#         converted.save(filename='test_converted.jpg')
#         pass
    
    
##>>> with image.clone() as resize:
##...     resize.resize(234, 234)
##...     resize.save(filename='seam-resize.jpg')
##...     resize.size
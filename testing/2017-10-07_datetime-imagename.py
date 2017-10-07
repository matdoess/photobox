from datetime import datetime

def imagename():
        imagepath = 'pics/'
        imagedatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        imagesuffix = '_Test'
        imageext = '.jpg'
        imagenamecomplete = imagepath + imagedatetime + imagesuffix + imageext
        return imagenamecomplete
    
iname = imagename()
print(iname)
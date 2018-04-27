from datetime import datetime

def imagename(imagesuffix2=""):
    imagepath = 'pics/'
    imagedatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    imagesuffix = '_Hochzeit-EJ'
    if imagesuffix2 != "":
        #print ('if is true')
        imagesuffix2 = '_' + imagesuffix2
        #print(imagesuffix2)
    imageext = '.jpg'
    imagenamecomplete = imagepath + imagedatetime + imagesuffix + imagesuffix2 + imageext
    return imagenamecomplete
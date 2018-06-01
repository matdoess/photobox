from wand.image import Image

##with Image(filename='test.jpg') as original:
##    with original.convert('png') as converted:
##        pass
    
##with Image(filename='test.jpg') as img:
##    print('width =', img.width)
##    print('height =', img.height)

with Image(filename='test.jpg') as original:
    with original.clone() as converted:
        converted.transform(resize='1500^>')
        #converted.sample(1500,2000)
        converted.compression_quality = 80
        converted.save(filename='test_converted.jpg')
        pass
    
    
##>>> with image.clone() as resize:
##...     resize.resize(234, 234)
##...     resize.save(filename='seam-resize.jpg')
##...     resize.size
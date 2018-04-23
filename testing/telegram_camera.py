#import io
from io import BytesIO
import time
import picamera

# Create an in-memory stream
my_stream = BytesIO()
my_stream.name = 'photobox-sos.jpg'

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    #camera.preview.alpha = 0
    # Camera warm-up time
    time.sleep(2)
    camera.capture(my_stream, 'jpeg')
    camera.stop_preview()

my_stream.seek(0)


# Telegram
import telegram
matthias_doess = 515880313
johannes_lerch = 204019701
help_person_id = johannes_lerch

#image.save(bio, 'JPEG')
#bio.seek(0)

bot = telegram.Bot(token='346412359:AAF6xZX-dmUMjjFE9ToX1822wMbwxCNvM9E')
#print(bot.get_me())
bot.send_message(chat_id=help_person_id, text="Photobox SOS")
bot.send_photo(chat_id=help_person_id, photo=my_stream)

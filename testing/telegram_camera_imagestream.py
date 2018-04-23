#import io
from io import BytesIO
import time
from Camera import Camera


# Create Imagestream Objekt and Take Picture
camera = Camera()
camera.stream()
# Bild wird in camera.imagestream gespeichert

# Telegram
import telegram
matthias_doess = 515880313
johannes_lerch = 204019701
help_person_id = matthias_doess

#image.save(bio, 'JPEG')
#bio.seek(0)

print("Create BOT start")
bot = telegram.Bot(token='346412359:AAF6xZX-dmUMjjFE9ToX1822wMbwxCNvM9E')
print("Create BOT end")
#print(bot.get_me())
print("Send message start")
bot.send_message(chat_id=help_person_id, text="Photobox SOS")
print("Send image start")
bot.send_photo(chat_id=help_person_id, photo=camera.imagestream)
print("Send ENDE")

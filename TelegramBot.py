import settings

import telegram
from datetime import datetime

class TelegramBot():

        chat_id = settings.myList['private_config']['telegram']['help_person_id']

        #image.save(bio, 'JPEG')
        #bio.seek(0)

        print("Create BOT start")
        bot = telegram.Bot(token=settings.myList['private_config']['telegram']['api-token'])
        print("Create BOT end")
        #print(bot.get_me())
        print("Send message start")
        bot.send_message(chat_id, text=settings.myList['config']['text']['photobox_sos'])
        print("Send image start")
        bot.send_photo(chat_id, photo=camera.imagestream)
        print("Send ENDE")
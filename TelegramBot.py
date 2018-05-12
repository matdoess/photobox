import settings

import telegram
import pickle
from os.path import isfile
from datetime import datetime


class TelegramBot():

    if not isfile('objects/help_person.dict'):
        help_person = {}
        print('ERROR: object help_person.dict does not exist')

    help_person = pickle.load( open( "objects/help_person.dict", "rb" ) )
    print(help_person)
    text = ""
    photo = ""

    def send(self):
        bot = telegram.Bot(token=settings.myList['private_config']['telegram']['api-token'])

        for chat_id in self.help_person:
            bot.send_message(chat_id, self.text)
            bot.send_photo(chat_id, self.photo)


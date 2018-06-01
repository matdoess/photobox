import settings

import telegram
import pickle
from os.path import isfile
from datetime import datetime

from PIL import Image
from io import BytesIO

class TelegramBot():

    if not isfile('objects/help_person.dict'):
        help_person = {}
        print('ERROR: object help_person.dict does not exist')

    help_person = pickle.load( open( "objects/help_person.dict", "rb" ) )
    print(help_person)
    text = ""
    photo = ""

    def updateHelpPerson(self):
        self.help_person = pickle.load( open( "objects/help_person.dict", "rb" ) )

    def send(self):
        bot = telegram.Bot(token=settings.myList['private_config']['telegram']['api-token'])
        print(self.help_person)

        for chat_id in self.help_person:
            bot.send_message(chat_id, self.text, timeout=20)
            bot.send_photo(chat_id, self.photo, timeout=40)
            # Für mehrfaches Versenden an Anfang des Bildes springen
            self.photo.seek(0)


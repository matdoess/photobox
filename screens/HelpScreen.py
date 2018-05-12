from kivy.uix.screenmanager import Screen

from Camera import Camera
from TelegramBot import TelegramBot
from datetime import datetime

import settings

class HelpScreen(Screen):
    def on_pre_enter(self):
        self.ids.HelpImageId.source = settings.myList['config']['images']['help_person']
        self.ids.HelpScreenLabel.text = settings.myList['config']['text']['help_text']

    def sending_help(self):
        self.ids.HelpScreenLabel.text = settings.myList['config']['text']['help_sending_text']  

    def send_help(self):
        print("send_help ausgeführt")

        # Create Imagestream Objekt and Take Picture
        camera = Camera()
        camera.stream()
        # Bild wird in camera.imagestream gespeichert

        telegrambot = TelegramBot()
        senddatetime = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
        telegrambot.text = settings.myList['config']['text']['photobox_sos'] + ' [' + senddatetime + ']'
        telegrambot.photo = camera.imagestream
        telegrambot.send()

        # # Telegram
        # import telegram
        # chat_id = settings.myList['private_config']['telegram']['help_person_id']

        # #image.save(bio, 'JPEG')
        # #bio.seek(0)

        # print("Create BOT start")
        # bot = telegram.Bot(token=settings.myList['private_config']['telegram']['api-token'])
        # print("Create BOT end")
        # #print(bot.get_me())
        # print("Send message start")
        # bot.send_message(chat_id, text=settings.myList['config']['text']['photobox_sos'])
        # print("Send image start")
        # bot.send_photo(chat_id, photo=camera.imagestream)
        # print("Send ENDE")

        self.ids.HelpScreenLabel.text = settings.myList['config']['text']['help_success_text']    

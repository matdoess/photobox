import configparser

config = configparser.ConfigParser()
config.read('./config/global-config.ini')

private_config = configparser.ConfigParser()
private_config.read('./config/private-config.ini')

from kivy.config import Config
Config.read(config['kivy']['config_file'])

import sys

import settings

from telegram.ext import Updater, CommandHandler
import pickle
from os.path import isfile


# Environment festlegen
env = sys.argv[1] if len(sys.argv) > 1 else 'raspberrypi'

# Environment in globale Liste schreiben
settings.myList["env"] = env

# Config in globale Variable schreiben
settings.myList['config'] = config._sections

# Private_Config in globale Variable schreiben
settings.myList['private_config'] = private_config._sections



if not isfile('objects/help_person.dict'):
    help_person = {}
    pickle.dump( help_person, open( "objects/help_person.dict", "wb"))

help_person = pickle.load( open( "objects/help_person.dict", "rb" ) )
print(help_person)

updater = Updater(settings.myList['private_config']['telegram']['api-token'])

def save_chat_id(bot, update):
    update.message.reply_text(
        'Hello {}. You have been added as "Photobox Help Person".\nSend /end to get removed from the list.\nSend /status to see the list.'.format(update.message.from_user.first_name))
    #print("chat_id")
    #print(update.message.chat_id)
    #print(update.message.from_user.username)
    help_person[update.message.chat_id]=update.message.from_user.username
    #print(bot)
    print(help_person)
    pickle.dump( help_person, open( "objects/help_person.dict", "wb"))

def delete_chat_id(bot, update):
    update.message.reply_text(
        'Hello {}. You have been removed from the "Photobox Help Person" list.'.format(update.message.from_user.first_name))
    #print("chat_id")
    #print(update.message.chat_id)
    del help_person[update.message.chat_id]
    print(help_person)
    pickle.dump( help_person, open( "objects/help_person.dict", "wb"))

def status_help_persons(bot, update):
    update.message.reply_text(
        'Registered Help Persons:\n{}'.format(help_person))
    print(help_person)


updater.dispatcher.add_handler(CommandHandler('start', save_chat_id))
updater.dispatcher.add_handler(CommandHandler('end', delete_chat_id))
updater.dispatcher.add_handler(CommandHandler('status', status_help_persons))

updater.start_polling()
updater.idle()
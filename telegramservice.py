from telegram.ext import Updater, CommandHandler
import pickle
from os.path import isfile


if not isfile('objects/help_person.dict'):
    help_person = {}
    pickle.dump( help_person, open( "objects/help_person.dict", "wb"))

help_person = pickle.load( open( "objects/help_person.dict", "rb" ) )
print(help_person)

updater = Updater(settings.myList['private_config']['telegram']['api-token'])

def save_chat_id(bot, update):
    update.message.reply_text(
        'Hello {}. You have been added as "Photobox Help Person". Send /end to get removed from the list.'.format(update.message.from_user.first_name))
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


updater.dispatcher.add_handler(CommandHandler('start', save_chat_id))
updater.dispatcher.add_handler(CommandHandler('end', delete_chat_id))

updater.start_polling()
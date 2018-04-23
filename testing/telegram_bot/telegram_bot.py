from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))



updater = Updater('346412359:AAF6xZX-dmUMjjFE9ToX1822wMbwxCNvM9E')

updater.dispatcher.add_handler(CommandHandler('hello', hello))



updater.start_polling()

updater.idle()

bot.sendMessage(chat_id='@matthias_doess', text="I'm a bot, please talk to me!")

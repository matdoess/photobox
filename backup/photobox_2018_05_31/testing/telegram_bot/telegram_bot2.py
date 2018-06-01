matthias_doess = 515880313
import telegram
bot = telegram.Bot(token='346412359:AAF6xZX-dmUMjjFE9ToX1822wMbwxCNvM9E')
print(bot.get_me())
bot.send_message(chat_id=matthias_doess, text="I'm a bot, please talk to me!")

# IDs
matthias_doess = 515880313
group_test = -194984597

import telepot
token = '346412359:AAF6xZX-dmUMjjFE9ToX1822wMbwxCNvM9E'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())
print(TelegramBot.getUpdates())
TelegramBot.sendMessage(group_test, 'I do not understand you, Sir!')


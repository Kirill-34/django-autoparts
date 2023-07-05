import telepot

token = '6221081603:AAEpuNdyV_ocSXguJDyAZ4EupSpMxQ4q6ss'
name = 'Autoparts'
username = 'AutopartsOilery_bot'
telegramBot = telepot.Bot(token)

def send_message(text):
    telegramBot.sendMessage(1084912803, text, parse_mode="Markdown")
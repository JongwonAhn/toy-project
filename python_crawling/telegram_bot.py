import telegram

bot = telegram.Bot(token = 'tokenNo')

#봇에서 메세지 읽기
# for i in bot.getUpdates():
#     print(i.message)

#봇에게 메세지 보내기
bot.sendMessage(chat_id = 5128747328, text = "testing...")

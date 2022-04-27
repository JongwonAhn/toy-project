import telegram

bot = telegram.Bot(token = '5396545974:AAEZl9YZY8pF2jye_dcJh_0oR_IfyDBZNAU')

#봇에서 메세지 읽기
# for i in bot.getUpdates():
#     print(i.message)

#봇에게 메세지 보내기
bot.sendMessage(chat_id = 5128747328, text = "testing...")

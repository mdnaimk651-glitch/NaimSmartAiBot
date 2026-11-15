import telebot

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalamu Alaikum! Ami Naim Smart AI Bot. Amake kichu jiggesh koro.")

@bot.message_handler(func=lambda m: True)
def reply(message):
    text = message.text.lower()
    if "hi" in text or "hello" in text or "assalam" in text:
        bot.reply_to(message, "Hello! Kemon acho?")
    elif "ke tumi" in text or "tomar nam" in text:
        bot.reply_to(message, "Ami Naim Smart AI Bot, Naim er banano.")
    elif "kemon acho" in text:
        bot.reply_to(message, "Ami valo achi! Tumi kemon acho?")
    else:
        bot.reply_to(message, "Tumi bolso: " + message.text + "\n\nAmi ekhono shikhtesi, aro smart hobo!")

bot.infinity_polling()

import telebot
import os
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is Running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalamu Alaikum! Ami Naim Smart AI Bot.")

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
        bot.reply_to(message, "Tumi bolso: " + message.text)

def run_bot():
    bot.infinity_polling()

Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalamu Alaikum! 🤖\n"
        "Ami Naim Smart AI Bot - ekhon ami asol AI!\n\n"
        "Amake jekono proshno koro:\n"
        "• Golpo likhe dao\n"
        "• Homework kore dao\n"
        "• Bangladesh er rajdhani koi?\n"
        "• Code likhe dao\n\n"
        "Bangla / English sob bujhi!"
    )

async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_chat_action("typing")
    
    try:
        prompt = f"""
        Tumi Naim Smart AI Bot. Tumi khub friendly, mojar, smart.
        User jodi Bangla te likhe (Banglish holeo), tumi Bangla tei uttor diba.
        User jodi English e likhe, English e uttor diba.
        Choto choto kore sundor kore bujhiye diba, boro rochona likhba na.
        Tumi LDR NAIM_TOP er banano bot.

        User er proshno: {user_text}
        """
        response = model.generate_content(prompt)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Ektu problem hoise dost, abar try koro. 😅")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_reply))
print("Bot is Running...")
app.run_polling()

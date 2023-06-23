import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ""
    with open('messages/start.html', 'r') as reader:    
        message = reader.read()
    await context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="HTML",text=message)

async def get_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://icanhazdadjoke.com/", headers = {"Accept": "application/json"})
    print(response.json())
    joke = response.json()["joke"]
    await context.bot.send_message(chat_id=update.effective_chat.id,text=joke)


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    joke_handler = CommandHandler('joke', get_joke)
    application.add_handler(joke_handler)
    
    application.run_polling()
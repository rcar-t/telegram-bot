import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import controller

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ""
    with open('messages/start.html', 'r') as reader:    
        message = reader.read()
    await context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="HTML",text=message)


def start_bot():
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
    


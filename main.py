import asyncio
from dotenv import load_dotenv
from threading import Thread

import controller
import telegram_bot
from telegram_broadcast import initiate_cat_health_subscription

if __name__ == '__main__':
    load_dotenv()
    initiate_cat_health_subscription()
    # Thread(target = initiate_cat_health_subscription).start()
    # Thread(target = controller.initialise_endpoint).start()
    # Thread(target = telegram_bot.start_bot).start()


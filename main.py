import asyncio
from dotenv import load_dotenv

import controller
from telegram_broadcast import initiate_cat_health_subscription

def main():
    load_dotenv()
    controller.initialise_endpoint()
    asyncio.run(initiate_cat_health_subscription())

if __name__ == '__main__':
    main()
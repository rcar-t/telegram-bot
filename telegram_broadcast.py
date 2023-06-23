import telegram
import asyncio
import os
from dotenv import load_dotenv

from graphql_subscription import get_graphql_client
import utils

def get_bot():
    return telegram.Bot(os.getenv("TELEGRAM_TOKEN"))

def initiate_cat_health_subscription():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(subscribe())
    loop.close()

async def subscribe():
    print("cat health subscription initialising") 
    query = """
        subscription LatestCatHealthState {
            latestCatHealthState {
                status
                timestamp
            }
        }
    """
    client = get_graphql_client()
    await client.subscribe(query=query, handle=send_cat_health_alerts)

nok_start_time=0

def send_cat_health_alerts(payload): 
    data = payload["data"]["latestCatHealthState"]
    if data["status"] == "NOK":
        # if nok_start_time == 0:
        #     nok_start_time = int(data["timestamp"])
        datetime = utils.long_to_datetime(int(data["timestamp"]))
        message = f"NOK detected for CAT-ND at {datetime}."
        asyncio.create_task(send_message(message))
    else : 
        nok_start_time = 0
        asyncio.create_task(send_message(data))

async def send_message(payload, parse_mode="", chat_id=""):
    bot = get_bot()
    channel = chat_id if len(chat_id) != 0 else os.getenv("NOTIFICATION_CHANNEL_NAME")
    async with bot: 
        await bot.send_message(text=payload, parse_mode=parse_mode, chat_id=channel)
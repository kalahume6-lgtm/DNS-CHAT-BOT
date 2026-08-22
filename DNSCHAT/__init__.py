import logging
import time
import asyncio
import os
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode
import config

asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
boot = time.time()

if not config.MONGO_URL:
    LOGGER.error("MONGO_URL is not set! Please set it in environment variables.")
    raise SystemExit("MONGO_URL missing")

mongodb = MongoCli(config.MONGO_URL)
db = mongodb.Anonymous
mongo = MongoClient(config.MONGO_URL)
OWNER = config.OWNER_ID
_boot_ = time.time()

class DNSCHAT(Client):
    def __init__(self):
        if not config.API_ID or not config.API_HASH or not config.BOT_TOKEN:
            raise SystemExit("API_ID, API_HASH or BOT_TOKEN is missing!")
        super().__init__(
            name="DNSCHAT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " + (self.me.last_name or "") # <- Yahi fix ki
        self.username = self.me.username
        self.mention = self.me.mention
        LOGGER.info(f"Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

DNSCHAT = DNSCHAT()

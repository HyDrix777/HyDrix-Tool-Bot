import logging
import os

from pyrogram import Client, idle

from lib.config import API_HASH, API_ID, BOT_TOKEN
from lib.tg_stream import app, call_py

if os.path.exists("log.txt"):
    with open("log.txt", "r+") as f:
        f.truncate(0)

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="[%X]",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="lib.driver"),
)

LOGGER.info("Starting bot...")
bot.start()
app.start()
call_py.start()
LOGGER.info("Bot has been started!")
idle()

from pyrogram import Client
import os
from pytgcalls import PyTgCalls
from infog import SESSION_NAME




BOT_TOKEN = os.environ.get("BOT_TOKEN", "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w")
API_ID = int(os.environ.get("API_ID", "18891187"))
API_HASH = os.environ.get("API_HASH", "7d120384f48b2a86fa2b9e9772a28af6")


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    Client = Client(
        "Pyrogram Bot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
   )

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,

call_py = PyTgCalls(user, overload_quiet_mode=True)
Client.run()

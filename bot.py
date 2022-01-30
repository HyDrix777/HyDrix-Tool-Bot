from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5139527038:AAF_vx72GV0xK9GvOg3ut3vIF-J6zxlmGGE")
API_ID = int(os.environ.get("API_ID", "18891187"))
API_HASH = os.environ.get("API_HASH", "7d120384f48b2a86fa2b9e9772a28af6")
MUST_JOIN = os.environ.get("MUST_JOIN", "Music_Galaxy_Dl")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "Pyrogram Bot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        must_join=MUST_JOIN,
        plugins=plugins
   )

bot.run()

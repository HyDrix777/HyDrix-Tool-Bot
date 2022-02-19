from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w")
API_ID = int(os.environ.get("API_ID", "18891187"))
API_HASH = os.environ.get("API_HASH", "7d120384f48b2a86fa2b9e9772a28af6")
DATABASE_URL = os.environ.get("mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "Pyrogram Bot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
   )

bot.run()

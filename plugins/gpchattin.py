import os
from pyrogram import Client, filters

CHAT_ID = int(os.environ.get("-1001500208686", 0))
USER_ID = int(os.environ.get("784589736", 0))


@Client.on_message(filters.private & filters.all & filters.user(USER_ID))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)

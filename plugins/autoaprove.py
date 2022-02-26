from decouple import config
import os, asyncio, logging
from pyrogram import Client, filters, idle
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait, MessageNotModified


logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.INFO,
    datefmt="[%d/%m/%Y %H:%M:%S]",
    format=" %(asctime)s - [INDOAPPROVEBOT] >> %(levelname)s << %(message)s",
    handlers=[logging.FileHandler("indoapprovebot.log"), logging.StreamHandler()])

@Client.on_chat_join_request(filters.chat)
async def approve(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        logging.info(f"Sleeping for {e.x + 2} seconds due to floodwaits!")
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)



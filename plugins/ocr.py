import os
import pytesseract
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty



@Client.on_message(filters.private("ptt"))
async def ptt(_, msg: Message):
    user_id = msg.from_user.id
    message_id = msg.message_id
    name_format = f"StarkBots_{user_id}_{message_id}"
    message = await msg.reply("Downloading and Extracting...")
    image = await msg.download(file_name=f"{name_format}.jpg")
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    text = text[:-1]
    try:
        await msg.reply(text, quote=True, disable_web_page_preview=True)
    except MessageEmpty:
        await msg.reply("Either the image has no text or the text is not recognizable.", quote=True)
    os.remove(image)

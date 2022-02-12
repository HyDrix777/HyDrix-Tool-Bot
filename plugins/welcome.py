import asyncio
from pyrogram import Client, filters as Worker

MENTION = "{}"  
MESSAGE = "{} Welcome to {}!" 

@Client.on_message(Worker.new_chat_members)
async def welcome(client, message):

    new_members = [MENTION.format(message.from_user.mention) for i in message.new_chat_members]

    dell=await message.reply_text(text, disable_web_page_preview=True)
    await asyncio.sleep(1000)
    await dell.delete()

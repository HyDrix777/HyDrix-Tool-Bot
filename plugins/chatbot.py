from pyrogram import *
import requests
import os
from pyrogram import Client, filters




@Client.on_message(filters.command(["chat"]))
async def chat (client , message):
    await message.reply_text(text = ''' I AM KANNA-CHAN ✨ 
    \n\n I AM YOUR VIRTUAL FRIEND ✨
    \n\nI CAN REPLY TO ANY TEXT MESSAGE YOU SEND✨''')

@Client.on_message()
async def kuki (client , message):
    msg = message.text
    r = requests.get(url = f"https://www.kuki-api.tk/api/message={msg} " )
    print(f"https://www.kuki-api.tk/api/message={msg}")
    data = r.json()
    print(data)
    await message.reply_text(data['reply'])

@Client.on_message(filters.command(["help"]))
async def support (client , message):
    await message.reply_text('join : @fossaf *blushes*')







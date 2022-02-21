import os
from pyrogram import Client, filters
from pyrogram.types import Message




@Clinte.on_message(filters.text & filters.Private) 
def echobot(cliente, message):
    message.replay_text(message.text)

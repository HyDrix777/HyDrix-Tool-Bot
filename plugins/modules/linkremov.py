import os 
import pyrogram
from pyrogram import Client, filters



@Client.on_message(filters.group & filters.regex("http") | filters.group & filters.regex("www") | filters.group & filters.regex("t.me"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return

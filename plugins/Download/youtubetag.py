import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags
from YoutubeTags import videotags





@Client.on_message(filters.group & filters.regex("https://www.youtube.com") | filters.group & filters.regex("http://www.youtube.com") | filters.group & filters.regex("https://youtu.be/") | filters.group & filters.regex("https://www.youtu.be/") | filters.group & filters.regex("http://www.youtu.be/"))
async def tag(bot, message):
    link = str(message.text)
    tags = videotags(link) 
    if tags=="":
         await message.reply_text(" Nᴏ ᴛᴀɢ ғᴏᴜɴᴅ 🔖")
    else:
         await message.reply_text(text=f"Tʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴛᴀɢs ᴜsᴇᴅ ғᴏʀ ᴛʜᴇ ᴠɪᴅᴇᴏ ʏᴏᴜ sᴇɴᴅ ᴍᴇ\n\n\n  {tags}  \n\n\n ♥️ Pᴏᴡᴇʀᴇᴅ ʙʏ : @HTGToolBot")

import random, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["genpass", 'genpw']))
async def password(bot, update):
    message = await update.reply_text(text="`Processing...`")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    try:
        limit = int(message.text)
    except:
        await message.edit_text('Limit is wrong')
        return
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @Music_Galaxy_Dl",
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Group', url='https://t.me/Music_Galaxy_Dl')]])
    await message.edit_text(text, True)

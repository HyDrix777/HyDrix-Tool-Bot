import random, os
from pyrogram import Client, filters




@Client.on_message(filters.private & filters.command("password"))
async def password(bot, update):
        await message.reply("Reply to a supported media file")
    message = await message.reply_text('`Processing...`')
    password = "abcdefghijklmnopqrstuvwxyz"+"1234567890"+"!@#$%^&*()_+".lower()
    
    try:
        limit = int(message.text)
    except:
        await message.edit_text('Limit is wrong')
        return
    
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @EKBOTZ_UPDATE"
    
    await message.edit_text(text, True)

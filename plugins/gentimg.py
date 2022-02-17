import os
import persondoesnotexist
import catdoesnotexist
from pyrogram import Client, filters





@Client.on_message(filters.private & filters.text)
async def start(bot, update):
    await update.reply_text(
        "Send /gan command with type for gan image"+"\n"+"/gan person - Person Image"+"\n"+"/gan cat - Cat Image"
    )


@Client.on_message(filters.private & filters.command("gan"))
async def gan(bot, update):
    
    if len(update.text.split()) <= 1:
        return
    
    type = update.text.split()[-1]
    
    if update.text == "person":
        image = persondoesnotexist.image('person.jpg')
    elif update.text == "/cat":
        image = catdoesnotexist.image('cat.jpg')
    else:
        return
    
    await update.reply_photo(image)
    
    try:
        os.remove(image)
    except:
        pass

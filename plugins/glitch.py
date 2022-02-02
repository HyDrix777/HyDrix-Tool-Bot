import os
import glitchart
from pyrogram import Client, filters



PATH = os.environ.get("PATH", "./DOWNLOADS")



@Client.on_message(filters.private("glitch"))
async def glitch(bot, update):
    if not message.reply_to_message:
        return await message.reply_text("Reply to some text.")
    download_path = PATH + "/" + str(update.from_user.id) + "/"
    download_location = download_path + "photo.jpg"
    message = await message.reply_text(
    m = await message.reply_text("Processing")
        disable_web_page_preview=True,
        quote=True
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @TheFayas.",
            disable_web_page_preview=True
        )
        return 
    await message.edit_text(
        text="`Converting to glitch art...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        await update.reply_photo(
            photo=glitch_art,
            caption=update.caption,
            quote=True
        )
        os.remove(download_location)
        os.remove(glitch_art)
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @TheFayas.",
            disable_web_page_preview=True
        )
        return
    await message.delete()

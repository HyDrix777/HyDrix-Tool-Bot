import os
from pyrogram import Client, filters


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")



@Client.on_message(filters.video & filters.private)
async def mp3(bot, message):
    
    # download video
    file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
    txt = await message.reply_text("Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ sᴇʀᴠᴇʀ...")
    await message.download(file_path)
    await txt.edit_text("Downloaded Successfully")
    
    # convert to audio
    await txt.edit_text("Cᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ.....")
    await message.reply_audio(audio=file_path, caption="@HTGToolBot", quote=True)
    
    # remove file
    try:
        os.remove(file_path)
    except:
        pass
    
    await txt.delete()

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file

@Client.on_message(filters.command(["tgmedia", "tgraph", "telegraph"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>Tᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="open link", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="share link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="🏃 Close", callback_data="delete")]
            ]
        )
    )
    finally:
        os.remove(download_location)

@Client.on_callback_query()
async def hydrix(bot, msg: CallbackQuery):
    if msg.data == "start":
        await msg.message.edit(
            text ="""Sooon...."""
        )

    elif msg.data == "delete":
        await msg.message.delete()


@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"𝗢𝗼𝗽𝘀 𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝗪𝗲𝗻𝘁 𝗪𝗿𝗼𝗻𝗴\n{error} Contact @HydraLivegrambot")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

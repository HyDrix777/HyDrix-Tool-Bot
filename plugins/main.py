import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from telegraph import upload_file
from pyrogram.types import CallbackQuery
import requests 
import lyricsgenius

import traceback
import logging
from pyrogram import StopPropagation, filters

import infog
from database.broadcast import broadcast
from database.check_user import handle_user_status
from database.databaseb import Database


LOG_CHANNEL = infog.LOG_CHANNEL
AUTH_USERS = infog.AUTH_USERS
DB_URL = infog.DB_URL
DB_NAME = infog.DB_NAME

db = Database(DB_URL, DB_NAME)




@Client.on_message(filters.private)
async def _(bot, message):
    await handle_user_status(bot, message)

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    # return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.reply_sticker(
        sticker="CAACAgQAAxkBAAIg5WIsoeHJ6NPJQWVJxYccrii6UHZdAAKgCAACp0h3Bfo4mn6VPDjmHgQ"             
    )
    await message.reply_text(
        text=f"✨ **ʜᴇʟʟᴏ** ||{message.from_user.mention}||!\n\n💭 ɪ'ᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ** [🛠️](https://telegra.ph/file/ea82bbb4deebdbf9d68e8.jpg)\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
           ],[
           InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ],[
           InlineKeyboardButton("🆎 ᴀʙᴏᴜᴛ", callback_data="about")  
           ],[
           InlineKeyboardButton("🤖 ᴍʏ ʙᴏᴛ's", callback_data="bots"),
           InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
           ]]
           )
       )

# Callback----------------

@Client.on_callback_query()
async def hydrix(bot, msg: CallbackQuery):
    if msg.data == "start":
        await msg.message.edit(
            text =f"""Sooon....🙄 ||പെവേർ ആയോ {msg.from_user.first_name} മോനൂസ് 😜||"""
        )

    elif msg.data == "srrt":
        await msg.message.edit(
            text=f"✨ ʜᴇʟʟᴏ {msg.from_user.mention} !\n\n💭 ɪ'ᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ** [🛠️](https://telegra.ph/file/ea82bbb4deebdbf9d68e8.jpg)\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!",
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
               ],[
               InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
               InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
               ],[
               InlineKeyboardButton("🆎 ᴀʙᴏᴜᴛ", callback_data="about")
               ],[
               InlineKeyboardButton("🤖 ᴍʏ ʙᴏᴛ's", callback_data="bots"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )
               
    elif msg.data == "about":
        await msg.message.edit(
            text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├[🤖](https://telegra.ph/file/65005f9a58ca27140cdc0.jpg) **Mʏ Nᴀᴍᴇ** : [ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ](https://t.me/HTGToolBot)\n├🧑‍💻 **Mʏ Dᴇᴠ** : [Hʏᴅʀɪx](https://t.me/HydraLivegrambot)\n├📢 **Cʜᴀɴɴᴇʟ** : [ᴛɢɢ](https://t.me/Tg_Galaxy)\n├👥 **Gʀᴏᴜᴘ** : [ᴍɢ](https://t.me/Music_Galaxy_Dl)\n├📡 **Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://Heroku.com)\n├🔣 **Language** : [ᴘʏᴛʜᴏɴ 𝟹](https://python.org/)\n├🥭 **Dᴀᴛᴀʙᴀsᴇ** : [ᴍᴀɴɢᴏ ᴅʙ](https://mongodb.com)\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "help":
        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention}\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg)__ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\n➥ __first thing! I'm just only created for this bot education parpose__ 😊",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("sᴛɪᴄᴋᴇʀ ɪᴅ", callback_data="stck"),
               InlineKeyboardButton("ᴄʟᴇᴀɴ sᴍ", callback_data="clsm"),
               InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘ", callback_data="tgph")
               ],[
               InlineKeyboardButton("sᴇᴀʀᴄʜ ʏᴛ", callback_data="srch"),
               InlineKeyboardButton("ᴊsᴏɴ", callback_data="jsn"),
               InlineKeyboardButton("ᴍᴘ𝟺 ᴛᴏ ᴍᴘ𝟹", callback_data="conv")
               ],[
               InlineKeyboardButton("ʟʏʀɪᴄs ᴅʟ", callback_data="lyrc"),
               InlineKeyboardButton("sᴏɴɢ ᴅʟ", callback_data="sdl"),
               InlineKeyboardButton("ᴠɪᴅᴇᴏ ᴅʟ", callback_data="vdl")
               ],[
               InlineKeyboardButton("ɢᴛʀᴀɴsʟᴀᴛᴏʀ", callback_data="gtra"),
               InlineKeyboardButton("ғᴜɴ", callback_data="Fns"),
               InlineKeyboardButton("ɪɴғᴏ", callback_data="ids")
               ],[
               InlineKeyboardButton("ʏᴛ ᴛʜᴜᴍʙ ᴅʟ", callback_data="ytthumb"),
               InlineKeyboardButton("ᴘᴀsᴛᴇ", callback_data="past"),
               InlineKeyboardButton("ᴛᴛs", callback_data="tts")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("ʜᴏᴍᴇ 🏠", callback_data="srrt"),
               InlineKeyboardButton("ɴᴇxᴛ ➡️", callback_data="next")
               ],[
               InlineKeyboardButton("✘─────ᴇxɪᴛ─────✘", callback_data="delete")
               ]]
            )
        )
# Next Module-------
    elif msg.data == "next":
        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention}\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg)__ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\n➥ __first thing! I'm just only created for this bot education parpose__ 😊",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="gith"),
               InlineKeyboardButton("ᴄᴏᴠɪᴅ", callback_data="covi"),
               InlineKeyboardButton("ғᴏʀᴡᴀʀᴅɪɴɢ", callback_data="forw")
               ],[
               InlineKeyboardButton("ᴘʟᴀʏ sᴛᴏʀᴇ", callback_data="plat"),
               InlineKeyboardButton("ʀᴇᴍᴏᴠᴇ ʙɢ", callback_data="rmbg"),
               InlineKeyboardButton("ɢʟɪᴛᴄʜ ᴀʀᴛ", callback_data="glit")
               ],[
               InlineKeyboardButton("ᴅʟᴇ ɪɴʟɪɴᴇ", callback_data="dinl"),
               InlineKeyboardButton("sʜᴀᴢᴀᴍ", callback_data="shaz"),
               InlineKeyboardButton("ᴇᴅɪᴛ ᴍsɢ ᴀʟᴇʀᴛ", callback_data="emsa")
               ],[
               InlineKeyboardButton("ʏᴛ ᴛᴀɢ ғɪɴᴅᴇʀ", callback_data="yttf"),
               InlineKeyboardButton("ᴘɪɴ", callback_data="pins"),
               InlineKeyboardButton("ᴘᴜʀɢᴇs", callback_data="purg")
               ],[
               InlineKeyboardButton("ᴘɪɴɢ", callback_data="pinj"),
               InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="mute"),
               InlineKeyboardButton("ɪᴍᴅʙ", callback_data="imbd")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
               InlineKeyboardButton("ʜᴏᴍᴇ 🏠", callback_data="srrt"),
               InlineKeyboardButton("ɴᴇxᴛ ➡️", callback_data="next2")
               ],[
               InlineKeyboardButton("✘─────ᴇxɪᴛ─────✘", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "next2":
        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention}\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg)__ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\n➥ __first thing! I'm just only created for this bot education parpose__ 😊",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("sᴛʏʟɪsʜ ᴛxᴛ", callback_data="styl"),
               InlineKeyboardButton("ʜᴀɴᴅᴡʀɪᴛ", callback_data="hand"),
               InlineKeyboardButton("ᴀʟɪᴠᴇ", callback_data="aliv")
               ],[
               InlineKeyboardButton("ᴘᴅғ ᴛᴏ ᴛᴇxᴛ", callback_data="pdft"),
               InlineKeyboardButton("ᴀᴜᴅɪᴏʙᴏᴏᴋ", callback_data="audi"),
               InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", callback_data="repo")
               ],[
               InlineKeyboardButton("ɴᴏ ʟɪɴᴋ's", callback_data="nlng"),
               InlineKeyboardButton("ᴍᴜsɪᴄ ᴛᴀɢ", callback_data="must"),
               InlineKeyboardButton("sᴛɪᴋʀ ᴛᴏ ɪᴍɢ", callback_data="stki")
               ],[
               InlineKeyboardButton("sʜᴀʀᴇ", callback_data="shar"),
               InlineKeyboardButton("ᴜʀʟ sʜᴏʀᴛ", callback_data="urls"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
               InlineKeyboardButton("ʜᴏᴍᴇ 🏠", callback_data="srrt"),
               InlineKeyboardButton("ɴᴇxᴛ ➡️", callback_data="start")
               ],[
               InlineKeyboardButton("✘─────ᴇxɪᴛ─────✘", callback_data="delete")
               ]]
            )
        )

# futures------
    elif msg.data == "stck":
        await msg.message.edit(
            text="[🖼️](https://telegra.ph/file/4080224664799812688b6.jpg)➥ **sᴛɪᴄᴋᴇʀ ɪᴅ**❓- __First send me the Sticker , and reply to sticker this command👉🏻__ /stickerid.\n\n📚 **Available Commands**\n\n- /stickerid : Reply to sticker",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "clsm":
        await msg.message.edit(
            text="[🗑️](https://telegra.ph/file/c311d906b5bb2db7cf03e.jpg)➥ **ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ** - __I Can Delete A Service message like join left and more,add me your group and promote it.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "tgph":
        await msg.message.edit(
            text="[📜](https://telegra.ph/file/d1d7357dc98aeb2253c2a.jpg)➥ **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ**\n\n__Send me any Photo,gif,png I'll Upload it into__ Telegra.ph\n\n📚 **Available Commands**\n\n/tgraph : use this command in reply to Photo,gif,png.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "srch":
        await msg.message.edit(
            text="🔎 **Search YouTube videos**\n\n📚 **Available Commands**\n\n➥ /ytsearch - __search **YouTube** videos__\n\nEg : `/ytsearch Alen Walker`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "jsn":
        await msg.message.edit(
            text="📚 **Available Command**\n\n[📑](https://telegra.ph/file/d0717d29431518ff9dc21.jpg)➥ /json - __Reply To Any Message To Get Json__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "conv":
        await msg.message.edit(
            text="[📹](https://telegra.ph/file/5489b184451feaf8411d0.jpg)➋🎵➥ **Mp4 to Mp3Conveter**\n\n__Send a Video for converting to Audio.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "lyrc":
        await msg.message.edit(
            text="[🎼](https://telegra.ph/file/12155873bb98142cc2759.jpg) Here is the help for **Lyrics Download:**\n\n📚 **Available Commands**\n\n➥ /lyric - __[Music Name] Searches Lyrics for the particular Music on web.__\n\nEg: `/lyric beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "sdl":
        await msg.message.edit(
            text="[🎵](https://telegra.ph/file/b785946b7ae9244a2580a.jpg) Here is the help for **Music Download**:\n\n📚 **Available Commands**\n\n➥ /s - __To download audio songs from YouTube, This only work in my PM.__\n/song - __use this command to fast download songs from YouTube__\n\nEg: `/s beggin`\n`/song beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "vdl":
        await msg.message.edit(
            text="📹 **Vedio download**\n\n📚 **Available Command**\n\n➥ /v - __To download Video from YouTube, video downloading is very slowly pls wait it.__\n/video - __use this command to fast download videos from YouTube__\n\nEg: `/v alone`\n`/video alone`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "gtra":
        await msg.message.edit(
            text="[💱](https://telegra.ph/file/e655830a9d113c27a28ee.jpg)➥ **Google Translator Bot**\n\n__**Google Translator** which means , A bot to help you translate text to few Languages from any other language in world.__\n\n__Google Translator bot is able to detect a wide variety of languages because he is a grand son of Google Translate API.__\n\n__You can use Google Translator in his private chat & Groups.__\n\n**How To Use**\n\n➥ /tr (language code) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs or my pm\n➥ 👇🏼Click **lang list** __botton to find your language code__.👇🏼",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
               InlineKeyboardButton("📜 ʟᴀɴɢ ʟɪsᴛ", callback_data="lagl")
               ]]
            )
        )
    elif msg.data == "lagl":
        await msg.message.edit(
            text="⍟────[ʟɪsᴛ]────⍟\n**List is in the form**\n__Language code => Language__\n\n`af` -> Afrikaans\n`sq` -> Albanian\n`am` -> Amharic\n`ar` -> Arabic\n`hy` -> Armenian\n`az` -> Azerbaijani\n`eu` -> Basque\n`be` -> Belarusian\n`bn` -> Bengali\n`bs` -> Bosnian\n`bg` -> Bulgarian\n`ca` -> Catalan\n`ceb` -> Cebuano\n`ny` -> Chichewa\n`zh`-`cn` -> Chinese\n`co` -> Corsican\n`hr` -> Croatian\n`cs` -> Czech\n`da` -> Danish\n`nl` -> Dutch\n`en` -> English\n`eo` -> Esperanto\n`et` -> Estonian\n`tl` -> Filipino\n`fi` -> Finnish\n`fr` -> French\n`fy` -> Frisian\n`gl` -> Galician\n`ka` -> Georgian\n`de` -> German\n`el` -> Greek\n`gu` -> Gujarati\n`ht` -> Haitian creole\n`ha` -> Hausa\n`haw` -> Hawaiian\n`iw` -> Hebrew\n`hi` -> Hindi\n`hmn` -> Hmong\n`hu` -> Hungarian\n`is` -> Icelandic\n`ig` -> Igbo\n`id` -> Indonesian\n`ga` -> Irish\n`it` -> Italian\n`ja` -> Japanese*\n`jw` -> Javanese\n`kn` -> Kannada\n`kk` -> Kazakh\n`km` -> Khmer\n`rw` -> Kinyarwanda\n`ko` -> Korean\n`ku` -> Kurdish (kurmanji)\n`ky` -> Kyrgyz\n`lo` -> Lao\n`la` -> Latin\n`lv` -> Latvian\n`lt` -> Lithuanian\n`lb` -> Luxembourgish\n`mk` -> Macedonian\n`mg` -> Malagasy\n`ms` -> Malay\n`ml` -> Malayalam\n`mt` -> Maltese\n`mi` -> Maori\n`mr` -> Marathi\n`mn` -> Mongolian\n`my` -> Myanmar\n`ne` -> Nepali\n`no` -> Norwegian\n`or` -> Oriya\n`ps` -> Pashto\n`fa` -> Persian\n`pl` -> Polish\n`pt` -> Portuguese\n`pa` -> Punjabi\n`ro` -> Romanian\n`ru` -> Russian\n`sm` -> Samoan*\n`gd` -> Scots gaelic\n`sr` -> Serbian\n`st` -> Sesotho\n`sn` -> Shona\n`sd` -> Sindhi\n`si` -> Sinhala\n`sk` -> Slovak\n`sl` -> Slovenian\n`so` -> Somali\n`es` -> Spanish\n`su` -> Sundanese\n`sw` -> Swahili\n`sv` -> Swedish\n`tg` -> Tajik\n`ta` -> Tamil\n`tt` -> Tatar\n`te` -> Telugu\n`th` -> Thai\n`tr` -> Turkish\n`tk` -> Turkmen\n`ug` -> Uighur\n`uk` -> Ukrainian\n`ur` -> Urdu\n`uz` -> Uzbek\n`vi` -> Vietnamese\n`cy` -> Welsh\n`xh` -> Xhosa\n`yi` -> Yiddish\n`yo` -> Yoruba\n`zu` -> Zulu \n\n⍟───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="gtra")
               ]]
            )
        )

    elif msg.data == "Fns":
        await msg.message.edit(
            text="»────[Fun]────»\n[🔻](https://telegra.ph/file/a3a5895a4e312e9f3d803.jpg) **Here is the help for the Fun module**:\n\n📚 **Available Commands**\n\n➥ /roll : __Roll a dice__\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n\n➥ /run : __reply a random string from an array of replie.__\n➥ /runml : __reply a random string from an Malayalam lang array of replie.__ \n➥ /lnm : __find your lucky number.__\n➥ /love : __Love__ 😘\n➥ /toss : __Tosses A coin__\n➥ /shrug : __get shrug XD__\n➥ /table : __get flip/unflip__ :v\n➥ /decide : __Randomly answers yes/no/maybe__.\n➥ /truth :__asks you a question__\n➥ /tord : __can be a truth or a dare__.\n➥ /dare : __gives you a dare__\n➥ /rather : __would you rather__\n➥ /goodnight : Good night 😴\n➥ /morning : good morning 😊🌄\n➥ /abuse : labuse 🤬\n➥ /cry : Cry 😭🥲\n➥ /anime : Anime",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ids":
        await msg.message.edit(
            text="[🆔](https://telegra.ph/file/8671a3c153c0f609dc697.jpg)➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ Fɪɴᴅᴇʀ**\n\n📚 **Available Commands**\n\n1. __Send any message to get your ID.__\n2. __Forward any message from any user/bot/channel/group or anonymous admins to get ID.__\n3. __Add in group / channel to get ID.__\n4. Use /id command:\n- in private: To get ID through username\n- in group/channel: To get ID of that chat\n5. Your DC❓ : Click /dc to get your DC.\n6. /info : this command to get your all information, only work my Pm.\n- /ginfo : this command to get your group information ℹ️, this only work in group.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "past":
        await msg.message.edit(
            text="📇➥ /paste [text] - Paste The Given Text On Pasty",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "tts":
        await msg.message.edit(
            text="[🗣️](https://telegra.ph/file/f1cf0da2397558752fba8.jpg) **ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ** - ᴛᴛs\n\n__A Module To Convert TEXT To Voice With Language Support__\n\n📚 **Available Command**\n\n⍟ /tts : __Reply To Any TEXT message I will Convert As Audio__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ytthumb":
        await msg.message.edit(
            text="🔴 **YouTube Thumbnail Dl**\n\nsᴇɴᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.\n\n📚 **Available Commands**\n\n/ytthumb use this command to Yt link, to get thumbnail.\nExample: `/ytthumb http://www.youtube.com/watch?v=HhjHYkPQ8F0`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )


    elif msg.data == "bots":
        await msg.message.edit(
            text="╭───────────⍟\n├──•**Mʏ ʙᴏᴛs ʟɪsᴛ**[📋](https://telegra.ph/file/6220090a10c440bd8a2d9.jpg)\n│\n├𝟙 `Stylish Text bot`\n├𝟚 `Youtube Dl bot`\n├𝟛 `Mention All bot`\n├𝟜 `URL Uploader bot`\n├𝟝 `Music Dl bot`\n├𝟞 `Google Translator bot`\n│\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("𝟙. Stylish Text bot", url="https://t.me/StylishText_X_Bot")
               ],[
               InlineKeyboardButton("𝟚. Youtube Dl bot", url="https://t.me/YouTubeDownloader7Bot")
               ],[
               InlineKeyboardButton("𝟛. Mention All bot", url="https://t.me/Mentionalltgtbot")
               ],[
               InlineKeyboardButton("𝟜. URL Uploader bot", url="https://t.me/UrlUploader_Xrobot")
               ],[
               InlineKeyboardButton("𝟝. Music Dl bot", url="https://t.me/Musicdowntgbot")
               ],[
               InlineKeyboardButton("𝟞. Google Translator bot", url="https://t.me/GTranslatorRobBot")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "gith":
        await msg.message.edit(
            text="[🐈](https://telegra.ph/file/d428512e34fd9594ab1c3.jpg) **GitHub**\n\n📚 **Available Commands**\n\n➥ /github - Get your [GitHub](https://github.com) profile in my PM\nEg: `/github Username`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "covi":
        await msg.message.edit(
            text="🌍 **Covid Information**\n\n__A Module To Find All Country Informations. Use This Module To Get Covid Informations Of All Countries__\n\n📚 **Available Commands**\n\n[🦠](https://telegra.ph/file/8dfbbf70b17e26d62b18c.jpg) ➥ /covid [country name] - __Use This Method To Get Covid Informations.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "forw":
        await msg.message.edit(
            text="📨 **Forward message remover**\n\n⍟ __I am automatically remove forward messages from group, add me your group and promote.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "plat":
        await msg.message.edit(
            text="[🧩](https://telegra.ph/file/42d7e70b678f4ea03e1b5.jpg) **ᴘʟᴀʏ sᴛᴏʀᴇ**\n\n⍟ __hey this is a play store module,\n__This will Search application details of any app and give play store download link.__\n\n📚 **Available Commands**\n\nClick here /playstore 👈🏼",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "rmbg":
        await msg.message.edit(
            text="🎴 **ᴘʜᴏᴛᴏ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇ**\n\n⍟ __I'm photo background remover, send me the photo i will send the photo without background__.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "glit":
        await msg.message.edit(
            text="🥴 **ɢʟɪᴛᴄʜ ᴀʀᴛ**\n\n⍟ __This module help you photo to glitch in group,Just send me the image in Group not pm__ 😁.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "dinl":
        await msg.message.edit(
            text="🤖 **ʀᴇᴍᴏᴠᴇ ɪɴʟɪɴᴇ ᴍᴇssᴀɢᴇ**\n\n⍟ __This module to automatically deletes Inline messages sent Through Bot in Group's__.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "shaz":
        await msg.message.edit(
            text="[🎶](https://telegra.ph/file/d67ebb887ee63d33d970c.jpg)➥ **Shazam Music Finder**\n\n__You have a part of a song, but could not find out what that song is?__\n__Here's the best solution for you. Just send me a audio file sample and I'll tell you what is that song.__\n\n📚 **Available Commands**\n\n**Step 1** : __Send me a Audio__\n\n**Step 2** : __Reply your to Audio with this__ /audify __command__\n/audify : __Reply to Audio__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "emsa":
        await msg.message.edit(
            text="📝 **Edit Message Alert**\n\n__A Telegram Bot to Show alert when someone edits a message in Group__\n",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "yttf":
        await msg.message.edit(
            text="🏷️ **YouTube Tag Finder**\n\n__A telegram Bot That can extract any YouTube video Tag easy__\n__first give me the yt **URL**, and i extract tag for U__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "pins":
        await msg.message.edit(
            text="📌 **Pin**\n\n__All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!__\n\n📚 **Available Commands**\n\n- /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.__\n- /unpin : __I can Unpin the current pinned message in silently.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "purg":
        await msg.message.edit(
            text="✴️ **Purge**\n\n__Here is the help for the **Purges** module:__\n\n - /purge: __deletes all messages between this and the replied to message.__\n__only work in group.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "pinj":
        await msg.message.edit(
            text="📍 Here is the help for **Ping**:\n\n➥ /ping - __Check if Bot is alive or not.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "mute":
        await msg.message.edit(
            text="🔕 **Mute & Unmute**\n\n__This module allows you to do mute & unmute in group easily, by exposing some common actions!__\n\n📚 **Available Commands**\n\n➥ /mute: Mute a user in group.\n➥ /unmute: Unmute a user in group.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "imbd":
        await msg.message.edit(
            text="🎞️ **Movie Information**\n\n__A Module To Get The Movie Informations. Use This Module To Get Movie Informations__\n\n[📚](https://telegra.ph/file/ceb40ac901886eb603c5a.jpg) **Available Commands**\n\n➥ /imdb : __Get The Film Information From IMDB Source__\n➥ /search : __Get The Movie Information From Various Sources__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "styl":
        await msg.message.edit(
            text="🖋️ **Stylish Text**\n\n__a module for stylish text__\n__i can help you to get stylish fonts.__\n__just send me the some text & Reply to a text message to make stylish Text.__\n\n📚 **Available Commands**\n\n➥ /text : __Reply to a text message as to make S Text__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "hand":
        await msg.message.edit(
            text="🖊️ **Handwriting**\n\n📚 **Available Commands**\n➥ /h your text",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "aliv":
        await msg.message.edit(
            text="🙄 **Alive**\n\n😒To Find Out If I'm 🤒Dead Or Not\n➥ /alive - dead or not",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "pdft":
        await msg.message.edit(
            text="📄 **Pdf to Text**\n\n- __a modular Telegram Bot which provides Pdf Tools using PyPdf2 Fork, Send me a pdf file to Move on.__\n\n📚 **Available Commands**\n\n➥ /pdf2txt : __Extract text to Txt file__\n➥ /pinfo : __to Get PDF information__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "audi":
        await msg.message.edit(
            text="📄➥🗣️ **Pdf to Audiobook**\n\n__A Telegram Bot which converts PDF TO Audio Using Pypdf2 and gTTS__\n__first Send Me a Pdf then im Convert to AudioBook__\n\n📚 **Available Commands**\n\n➥ /audiobook : __Please Reply to PDF file__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "repo":
        await msg.message.edit(
            text="🗳️ **Report**\n\n__ReportBoT help admins find Those who misbehave in Group.__\n__This command help you to report a message or a user to the admins of the group.__\n\n📚 **Available Commands**\n\n➥ /report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾).",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "nlng":
        await msg.message.edit(
            text="🔗🚫 **Remove URLs in group**\n\n__This module for who sends any kind of link ,remove all links from group.__\n\n➥ List of Links I delete!👇🏼\nhttps\nhttp\nt.me\nwww\ncom",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "must":
        await msg.message.edit(
            text="🔖 **Music tag adder**\n\ni can manage your music channel or group with some cool features like musics tags, getting a short demo of the musics and posting the musics artworks.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "stki":
        await msg.message.edit(
            text="🖼️➥ɪᴍɢ **Sticker to Image converter**\n\nYou can use this module to **Sticker to Image**,\nfirst send me the Sticker, then i give you a Image.\n\nDon't send me animated sticker or video sticker.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "shar":
        await msg.message.edit(
            text="✈️ **Share Text**\n\n📚 **Available Commands**\n\n➥ /share - __get shareable link of any text or link.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "urls":
        await msg.message.edit(
            text="⛓️ **𝖴𝗋𝗅 S𝗁𝗈𝗋𝗍𝗇𝖾𝗋**\n__This command help you to short a Url__\n\n📚 **Available Commands**\n\n➥ /short : __𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌__\n⍟ **Example**👇🏼\n/short https://t.me/Music_Galaxy_Dl",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "delete":
        await msg.message.delete()

# main commm--------

@Client.on_message(filters.group & filters.command("reload"))
async def reload(bot: Client, message: Message):
    await message.reply_text(
        text="✅ Bot restarted\n✅ Admin list updated!",
    )

@Client.on_message(filters.group & filters.edited)
async def edited(bot,message):
	chatid= message.chat.id	
	await bot.send_message(text=f"{message.from_user.mention} Edited This👉 [Message]({message.link})",chat_id=chatid)
	

@Client.on_message(filters.group & filters.command("help"))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text="Contact me in PM for help!",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("Click me for help!", url="https://t.me/HTGToolBot?start")
           ]]
           )
       )

@Client.on_message(filters.group & filters.command("start"))
async def start(bot: Client, message: Message):
    await message.reply_text(
        text="`Yes I'm still alive.`😌✨",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("Click me(◠ᴥ◕ʋ)", url="https://t.me/HTGToolBot?start")
           ]]
           )
       )

# G Translator Language code list

@Client.on_message(filters.private & filters.command("list"))
async def list(bot: Client, message: Message):
    await message.reply_text(
        text="he🙄🙄",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# Service clear--------------------

@Client.on_message(filters.service)
async def delete(bot,message):
 await message.delete()

#Inline search Remove---

@Client.on_message(filters.via_bot & filters.group)
async def inline(bot,message):
     await message.delete()

# Group forword rm------

@Client.on_message(filters.group & filters.forwarded)
async def forward(bot, message):
    await message.delete("This group doesn't allow forward messages")
    

#  Lyrics--------------------

@Client.on_message(filters.command("lyric"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("Sᴇᴀʀᴄʜɪɴɢ ʟʏʀɪᴄs...")
    query = query = message.text.split(None, 1)[1]
    x = "LtdSiWU2HM46_UHOTHje-yWnJYWGWpP9udmaSqu3GvGA8Z5Enzq6zh2OF-vwm3dv"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lʏʀɪᴄs ɴᴏᴛ ғᴏᴜɴᴅ...")
    xxx = f"""
**Lyrics Search Powered By ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ**
**Searched Song:** __{query}__
**Found Lyrics For:** __{S.title}__
**Artist:** {S.artist}
**Requested by:** {message.from_user.mention}
**Lyrics:**
{S.lyrics}"""
    await m.edit(xxx)

# Broadcast-----------

@Client.on_message(filters.command("settings"))
async def opensettings(bot, cmd):
    user_id = cmd.from_user.id
    await cmd.reply_text(
        f"`Here You Can Set Your Settings:`\n\nSuccessfully setted notifications to **{await db.get_notif(user_id)}**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                        callback_data="notifon",
                    )
                ],
                [InlineKeyboardButton("❎", callback_data="closeMeh")],
            ]
        ),
    )


@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)


@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        parse_mode="Markdown",
        quote=True
    )


@Client.on_message(filters.private & filters.command("ban_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban 🛑 any user from the bot 🤖.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."

        try:
            await c.send_message(
                user_id,
                f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**",
            )
            ban_log_text += "\n\nUser notified successfully!"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.private & filters.command("unban_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban 😃 any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )


@Client.on_message(filters.private & filters.command("banned_users"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"> **User_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)


@Client.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    user_id = cb.from_user.id
    if cb.data == "notifon":
        notif = await db.get_notif(cb.from_user.id)
        if notif is True:
            await db.set_notif(user_id, notif=False)
        else:
            await db.set_notif(user_id, notif=True)
        await cb.message.edit(
            f"`Here You Can Set Your Settings:`\n\nSuccessfully setted notifications to **{await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                            callback_data="notifon",
                        )
                    ],
                    [InlineKeyboardButton("❎", callback_data="closeMeh")],
                ]
            ),
        )
        await cb.answer(
            f"Successfully setted notifications to {await db.get_notif(user_id)}"
        )
    else:
        await cb.message.delete(True)

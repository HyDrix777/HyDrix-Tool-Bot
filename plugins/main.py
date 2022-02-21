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











@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    await message.reply_sticker(
        sticker="CAACAgIAAxkBAAIMVGIHmelSg0NoMQS4_Bc_aox2kcv1AAJuAANBtVYM0KWEcubcWogeBA"             
    )


    await message.reply_text(
        text=f"✨ **ʜᴇʟʟᴏ** ||{message.from_user.mention}||!\n\n💭 ɪ'ᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ** [🛠️](https://telegra.ph/file/738a362ee817361bbacd6.jpg)\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!",
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
            text ="""Sooon...."""
        )

    elif msg.data == "srrt":
        await msg.message.edit(
            text=f"✨ ʜᴇʟʟᴏ {msg.from_user.mention} !\n\n💭 ɪ'ᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ** [🛠️](https://telegra.ph/file/738a362ee817361bbacd6.jpg)\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!",
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
            text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├[🤖](https://telegra.ph/file/65005f9a58ca27140cdc0.jpg) **Mʏ Nᴀᴍᴇ** : [ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ](https://t.me/HTGToolBot)\n├🧑‍💻 **Mʏ Dᴇᴠ** : [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢 **Cʜᴀɴɴᴇʟ** : [ᴛɢɢ](https://t.me/Tg_Galaxy)\n├👥 **Gʀᴏᴜᴘ** : [ᴍɢ](https://t.me/Music_Galaxy_Dl)\n├📡 **Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://Heroku.com)\n├🔣 **Language** : [ᴘʏᴛʜᴏɴ 𝟹](https://python.org/)\n├🥭 **Dᴀᴛᴀʙᴀsᴇ** : [ᴍᴀɴɢᴏ ᴅʙ](https://mongodb.com)\n├📦 **sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ** : [sᴏᴜʀᴄᴇ](https://t.me/jsnssbssbddbssbdoeeeok)\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "help":
        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention}\n\n[🔰](https://telegra.ph/file/00651cac20faed3c7e3c1.jpg)__ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("sᴛɪᴄᴋᴇʀ", callback_data="stck"),
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
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start"),
               InlineKeyboardButton("soon..", callback_data="start")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "stck":
        await msg.message.edit(
            text="[🖼️](https://telegra.ph/file/4080224664799812688b6.jpg)➥ **sᴛɪᴄᴋᴇʀ ɪᴅ**❓- __Just send me the Sticker I would reply with it's Id__.",
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
            text="[📜](https://telegra.ph/file/d1d7357dc98aeb2253c2a.jpg)➥ **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ**\n\n__Send me any Photo,gif,png I'll Upload it into__ Telegra.ph\n\n📚 **Avaible Commands**\n\n/tgraph : use this command in reply to Image",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "srch":
        await msg.message.edit(
            text="🔎 **Search YouTube videos**\n\n📚 **Avaible Commands**\n\n➥ /search - __search **YouTube** videos__\n\nEg : `/search Alen Walker`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "jsn":
        await msg.message.edit(
            text="📚 **Avaible Command**\n\n[📑](https://telegra.ph/file/d0717d29431518ff9dc21.jpg)➥ /json - __Reply To Any Message To Get Json__",
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
            text="[🎼](https://telegra.ph/file/12155873bb98142cc2759.jpg) **Lyrics Download**\n\n📚 **Avaible Commands**\n\n➥ /lyric - __Send me a Song name I give you a Lyrics.__\n\nEg: `/lyric beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "sdl":
        await msg.message.edit(
            text="[🎵](https://telegra.ph/file/b785946b7ae9244a2580a.jpg) **Music Download**\n\n📚 **Avaible Commands**\n\n➥ /s - __To download audio songs from YouTube, This only work in my PM.__\n\nEg: `/s beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "vdl":
        await msg.message.edit(
            text="📹 **Vedio download**\n\n📚 **Avaible Command**\n\n➥ /v - __To download Video from YouTube, video downloading is very slowly pls wait it.__\n\nEg: `/v alone`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "gtra":
        await msg.message.edit(
            text="[💱](https://telegra.ph/file/e655830a9d113c27a28ee.jpg)➥ **Google Translator Bot**\n\n__**Google Translator** which means , A bot to help you translate text to few Languages from any other language in world.__\n\n__Google Translator bot is able to detect a wide variety of languages because he is a grand son of Google Translate API.__\n\n__You can use Google Translator in his private chat & Groups.__\n\n**How To Use**\n\n➥ Click /list __to find your language code__.\n\n➥ /tr (language code) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs or my pm",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "Fns":
        await msg.message.edit(
            text="⍟────[Fun]────⍟\n[🔻](https://telegra.ph/file/a3a5895a4e312e9f3d803.jpg) **Here is the help for the Fun module**:\n\n📚 **Avaible Commands**\n\n➥ /roll : __Roll a dice__\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n\n➥ /run : __reply a random string from an array of replie.__\n➥ /runml : __reply a random string from an Malayalam lang array of replie.__ \n➥ /lnm : __find your lucky number.__\n➥ /love : __Love__ 😘\n➥ /toss : __Tosses A coin__\n➥ /shrug : __get shrug XD__\n➥ /table : __get flip/unflip__ :v\n➥ /decide : __Randomly answers yes/no/maybe__.\n➥ /truth :__asks you a question__\n➥ /tord : __can be a truth or a dare__.\n➥ /dare : __gives you a dare__\n➥ /rather : __would you rather__\n➥ /goodnight : Good night 😴\n➥ /morning : good morning 😊🌄\n➥ /abuse : labuse 🤬\n➥ /cry : Cry 😭🥲\n/ping\n⍟───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ids":
        await msg.message.edit(
            text="[🆔](https://telegra.ph/file/8671a3c153c0f609dc697.jpg)➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ Fɪɴᴅᴇʀ**\n\n📚 **Avaible Commands**\n\n1. __Send any message to get your ID.__\n2. __Forward any message from any user/bot/channel/group or anonymous admins to get ID.__\n3. __Add in group / channel to get ID.__\n4. Use /id command:\n- in private: To get ID through username\n- in group/channel: To get ID of that chat\n5. Your DC❓ : Click /dc to get your DC.\n6. /info : this command to get your all information, only work my Pm.\n- /ginfo : this command to get your group information ℹ️, this only work in group.",
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
            text="[🗣️](https://telegra.ph/file/f1cf0da2397558752fba8.jpg) **ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ** - ᴛᴛs\n\n__A Module To Convert TEXT To Voice With Language Support__\n\n📚 **Avaible Command**\n\n⍟ /tts : __Reply To Any TEXT message I will Convert As Audio__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ytthumb":
        await msg.message.edit(
            text="🔴 **YouTube Thumbnail Dl**\n\nsᴇɴᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.\n\n📚 **Avaible Commands**\n\n/ytthumb use this command to Yt link, to get thumbnail.\nExample: `/ytthumb http://www.youtube.com/watch?v=HhjHYkPQ8F0`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )


    elif msg.data == "bots":
        await msg.message.edit(
            text="╭───────────⍟\n├──•**Mʏ ʙᴏᴛs ʟɪsᴛ**[📋](https://telegra.ph/file/6220090a10c440bd8a2d9.jpg)\n│\n├𝟙 `Stylish Text bot`\n│\n├𝟚 `Youtube Dl bot`\n│\n├𝟛 `Youtube Playlist dl bot`\n│\n├𝟜 `Mention All bot`\n│\n├𝟝 `URL Uploader bot`\n│\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("𝟙. Stylish Text bot", url="https://t.me/StylishText_X_Bot")
               ],[
               InlineKeyboardButton("𝟚. Youtube Dl bot", url="https://t.me/YouTubeDownloader7Bot")
               ],[
               InlineKeyboardButton("𝟛. Youtube Playlist dl bot", url="https://t.me/YoutubePlaylistdowntgbot")
               ],[
               InlineKeyboardButton("𝟜. Mention All bot", url="https://t.me/Mentionalltgtbot")
               ],[
               InlineKeyboardButton("𝟝. URL Uploader bot", url="https://t.me/UrlUploader_Xrobot")
               ],[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("🏃 ᴇxɪᴛ", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "gith":
        await msg.message.edit(
            text="[🐈](https://telegra.ph/file/d428512e34fd9594ab1c3.jpg) **GitHub**\n\n📚 **Avaible Commands**\n\n➥ /github - Get your [GitHub](https://github.com) profile in my PM\nEg: `/github Username`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "covi":
        await msg.message.edit(
            text="🌍 **Covid Information**\n\n__A Module To Find All Country Informations. Use This Module To Get Covid Informations Of All Countries__\n\n📚 **Avaible Commands**\n\n[🦠](https://telegra.ph/file/8dfbbf70b17e26d62b18c.jpg) ➥ /covid [country name] - __Use This Method To Get Covid Informations.__",
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
            text="[🧩](https://telegra.ph/file/42d7e70b678f4ea03e1b5.jpg) **ᴘʟᴀʏ sᴛᴏʀᴇ**\n\n⍟ __hey this is a play store module,\n__This will Search application details of any app and give play store download link.__\n\n📚 **Avaible Commands**\n\nClick here /playstore 👈🏼",
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
            text="[🎶](https://telegra.ph/file/d67ebb887ee63d33d970c.jpg)➥ **Shazam Music Finder**\n\n__You have a part of a song, but could not find out what that song is?__\n__Here's the best solution for you. Just send me a audio file sample and I'll tell you what is that song.__\n\n📚 **Avaible Commands**\n\n**Step 1** : __Send me a Audio__\n\n**Step 2** : __Reply your to Audio with this__ /audify __command__\n/audify : __Reply to Audio__",
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

    elif msg.data == "delete":
        await msg.message.delete()

# main commm--------

@Client.on_message(filters.group & filters.command("reload"))
async def reload(bot: Client, message: Message):
    await message.reply_text(
        text="✅Bot successfully reloaded!",
    )

@Client.on_message(filters.edited)
async def edited(bot,message):
	chatid= message.chat.id	
	await bot.send_message(text=f"{message.from_user.mention} Edited This👉 [Message]({message.link})",chat_id=chatid)
	

@Client.on_message(filters.group & filters.command("help"))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text="Contact me in PM for help!",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("Click me for help!", url="https://t.me/HTGToolBot")
           ]]
           )
       )

@Client.on_message(filters.group & filters.command("start"))
async def start(bot: Client, message: Message):
    await message.reply_text(
        text="`Yes I'm alive.`✨",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("Click me(◠ᴥ◕ʋ)", url="https://t.me/HTGToolBot")
           ]]
           )
       )

# G Translator Language code list

@Client.on_message(filters.private & filters.command("list"))
async def list(bot: Client, message: Message):
    await message.reply_text(
        text="⍟────[ʟɪsᴛ]────⍟\n**List is in the form**\n__Language code => Language__\n\n`af` -> Afrikaans\n`sq` -> Albanian\n`am` -> Amharic\n`ar` -> Arabic\n`hy` -> Armenian\n`az` -> Azerbaijani\n`eu` -> Basque\n`be` -> Belarusian\n`bn` -> Bengali\n`bs` -> Bosnian\n`bg` -> Bulgarian\n`ca` -> Catalan\n`ceb` -> Cebuano\n`ny` -> Chichewa\n`zh`-`cn` -> Chinese\n`co` -> Corsican\n`hr` -> Croatian\n`cs` -> Czech\n`da` -> Danish\n`nl` -> Dutch\n`en` -> English\n`eo` -> Esperanto\n`et` -> Estonian\n`tl` -> Filipino\n`fi` -> Finnish\n`fr` -> French\n`fy` -> Frisian\n`gl` -> Galician\n`ka` -> Georgian\n`de` -> German\n`el` -> Greek\n`gu` -> Gujarati\n`ht` -> Haitian creole\n`ha` -> Hausa\n`haw` -> Hawaiian\n`iw` -> Hebrew\n`hi` -> Hindi\n`hmn` -> Hmong\n`hu` -> Hungarian\n`is` -> Icelandic\n`ig` -> Igbo\n`id` -> Indonesian\n`ga` -> Irish\n`it` -> Italian\n`ja` -> Japanese*\n`jw` -> Javanese\n`kn` -> Kannada\n`kk` -> Kazakh\n`km` -> Khmer\n`rw` -> Kinyarwanda\n`ko` -> Korean\n`ku` -> Kurdish (kurmanji)\n`ky` -> Kyrgyz\n`lo` -> Lao\n`la` -> Latin\n`lv` -> Latvian\n`lt` -> Lithuanian\n`lb` -> Luxembourgish\n`mk` -> Macedonian\n`mg` -> Malagasy\n`ms` -> Malay\n`ml` -> Malayalam\n`mt` -> Maltese\n`mi` -> Maori\n`mr` -> Marathi\n`mn` -> Mongolian\n`my` -> Myanmar\n`ne` -> Nepali\n`no` -> Norwegian\n`or` -> Oriya\n`ps` -> Pashto\n`fa` -> Persian\n`pl` -> Polish\n`pt` -> Portuguese\n`pa` -> Punjabi\n`ro` -> Romanian\n`ru` -> Russian\n`sm` -> Samoan*\n`gd` -> Scots gaelic\n`sr` -> Serbian\n`st` -> Sesotho\n`sn` -> Shona\n`sd` -> Sindhi\n`si` -> Sinhala\n`sk` -> Slovak\n`sl` -> Slovenian\n`so` -> Somali\n`es` -> Spanish\n`su` -> Sundanese\n`sw` -> Swahili\n`sv` -> Swedish\n`tg` -> Tajik\n`ta` -> Tamil\n`tt` -> Tatar\n`te` -> Telugu\n`th` -> Thai\n`tr` -> Turkish\n`tk` -> Turkmen\n`ug` -> Uighur\n`uk` -> Ukrainian\n`ur` -> Urdu\n`uz` -> Uzbek\n`vi` -> Vietnamese\n`cy` -> Welsh\n`xh` -> Xhosa\n`yi` -> Yiddish\n`yo` -> Yoruba\n`zu` -> Zulu \n\n⍟───────────⍟",
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

@Client.on_message(filters.forwarded)
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
**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}
**__Lyrics:__**
{S.lyrics}"""
    await m.edit(xxx)

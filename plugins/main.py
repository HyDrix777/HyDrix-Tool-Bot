import os
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from telegraph import upload_file
import requests 
import lyricsgenius
import random




START_MSG = """
✨**Wᴇʟᴄᴏᴍᴇ** {message.from_user.mention} \n💭I ᴀᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ**\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!
"""

START_PHOTO = [
 "https://telegra.ph/file/e4901681616e47f1ab3bc.jpg",
 "https://telegra.ph/file/eba603c8799ea006d77be.jpg",
 "https://telegra.ph/file/f6f7beba68b77a6dbfb69.jpg",
 "https://telegra.ph/file/2333e8560d8d91203494c.jpg",
 "https://telegra.ph/file/2e4de7eb7fdda2576deb7.jpg"
]





@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, hydrix):
    await hydrix.reply_photo(
        photo=random.choice(START_PHOTO),
        caption=START_MSG.format(hydrix.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
           ],[
           InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", url="https://t.me/Tg_galaxy"),
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ],[
           InlineKeyboardButton(text="🔎 sᴇᴀʀᴄʜ ʏᴛ", switch_inline_query_current_chat=""),
           InlineKeyboardButton("🧑‍💻 ʙᴏᴛ ᴅᴇᴠ", url="https://t.me/Hydrix777")
           ],[
           InlineKeyboardButton("🏠 ʜᴏᴍᴇ", url="https://t.me/MusicdGalabdbxy_Dl"),
           InlineKeyboardButton("🚪 ᴇxɪᴛ", url="https://t.me/MusicdGalabdbxy_Dl")
           ]]
           )
       )

# Commands----------------

@Client.on_message(filters.private & filters.command("help"))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text="⍟─────[ᴄᴏᴍᴍ]─────⍟\n🔻**ᴍʏ ғᴜᴛᴜʀᴇs**🔻\n\n🖼️➥ **sᴛɪᴄᴋᴇʀ ɪᴅ**❓- Just send me the **Sticker** I would reply with it's Id.\n🗑➥ **ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ** - I Can Delete A **Service message** like join left and more,add me your group and promote it.\n📜➥ **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ** - Send me any **Photo** I'll Upload it into Telegra.ph\n🔎➥ You Can search **YouTube** videos in **nline Mode** | copy this and paste it `@HTGToolBot`\nOr\nsearch YT videos in this command👉🏻 /search\nEg : `/search bilever`\n🔰➥ /json - Reply To Any Message To Get Json\n📹➥🎵⍟ **Mp4** to **Mp3Conveter** - Send a **Video** for converting to **Audio**.\n\n🎼➥ /lyric - Send me a **Song name** I give you a Lyrics.\nEg: `/lyric beggin`\n🎵➥ /s - To **download** audio songs from **YouTube**,You can use this in group.\nEg : `/s Believer`\n📹➥ /v - To **download Video** from **YouTube**, video downloading is very slowly pls wait it.\n⚫➥ **ᴛɪᴋᴛᴏᴋ ᴅᴏᴡɴʟᴏᴀᴅ** - Send me **Tiktok** Video **Url** here\n💱➥ **Gᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ** - You can use me in group's in this command👉🏻 /tr first add me in group.\nClick /list to find your language.\nEg: reply to /tr en 👈🏼\n🕹️➥ **ғᴜɴ** - Click /fun to get fun commands\n\n🆔➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ Fɪɴᴅᴇʀ**\n1. Send any message to get **your ID**.\n2. Forward any message from any user/bot/channel or anonymous admins to get ID.\n3. Add in group / channel to get ID.\n4. **Use /id command:**\n- in private: To get ID through username\n- in group/channel: To get ID of that chat.\n5. **Your DC**❓ - Click /dc to get your DC.\n\n🆎⍟ /about - Know me 🙋\n⍟─────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )


# About--------------------

@Client.on_message(filters.private & filters.command("about"))
async def about(bot: Client, message: Message):
    await message.reply_text(
        text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖**Mʏ Nᴀᴍᴇ:** [Tg Tool Bot](https://t.me/HTGToolBot)\n├🧑‍💻**Mʏ Dᴇᴠ:** [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢**Cʜᴀɴɴᴇʟ:** [TGG](https://t.me/Tg_Galaxy)\n├👥**Gʀᴏᴜᴘ:** [MG](https://t.me/Music_Galaxy_Dl)\n├📡**Sᴇʀᴠᴇʀ:** [Heroku](https://Heroku.com)\n├🔣**Language:** [Python](https://python.org/)\n╰───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )


# Fun Comm-----------------

@Client.on_message(filters.command("fun"))
async def fun(bot: Client, message: Message):
    await message.reply_text(
        text="⍟────Fun────⍟\n🔻**Here is the help for the Fun module**:\n➥ /roll : Roll a dice\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n➥ /run : reply a random string from an array of replie.\n➥ /lnm : find your lucky number.\n ➥ /love : Love 😘\n➥ /toss : Tosses A coin\n➥ /shrug : get shrug XD\n➥ /table : get flip/unflip :v\n➥ /decide : \Randomly answers yes/no/maybe.\n⍟───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )


# Sticker id-----------------------

@Client.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is👇\n\n* `{message.sticker.file_id}` *", quote=True)


# Service clear--------------------

@Client.on_message(filters.service)
async def delete(bot,message):
 await message.delete()

@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
 await message.delete()


# Telegraph---------------------

@Client.on_message(filters.private & filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>ᴜᴘʟᴏᴀᴅɪɴɢ...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oᴏᴘs sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ\n{error} Cᴏɴᴛᴀᴄᴛ @HydraLivegrambot")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass



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

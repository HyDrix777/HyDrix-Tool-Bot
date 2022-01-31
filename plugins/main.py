import os
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from telegraph import upload_file
import requests 
import lyricsgenius



@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="╭──────────────⍟\n│Hᴇʏ 🧑🏻‍🔧\n│I ᴀᴍ Tg Tool Bot[🛠️](https://telegra.ph/file/0de314d6ed28fad848ccb.jpg)\n│I Have some cool futures✨\n│Click /help to know my Commands\n│and my uses 🍃\n╰──────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/HTGToolBot?startgroup=botstart")
           ],[
           InlineKeyboardButton("📢 Cʜᴀɴɴᴇʟ", url="https://t.me/Tg_galaxy"),
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ],[
           InlineKeyboardButton(text="🔎 Sᙓᗩᖇᙅᕼ", switch_inline_query_current_chat=""),
           InlineKeyboardButton("🧑‍💻 Bᴏᴛ Dᴇᴠ", url="https://t.me/Hydrix777")
           ],[
           InlineKeyboardButton("🏃 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )
@Client.on_message(filters.command("help"))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text="⍟─────[COM]─────⍟\n🔻My Futures🔻\n\n🖼️➥ **Sticker ID**❓- Just send me the Sticker I would reply with it's Id.\n🗑➥ **Clean Service message** - I Can Delete A **Service message** like join left and more,add me your group and promote it.\n📜➥ **Telegraph Uploader** - Send me any **Photo** I'll Upload it into Telegra.ph\n🔎➥ You Can search **YouTube** videos in **nline Mode** | copy this and paste it `@HTGToolBot`\n📹➥🎵⍟ **Mp4** to **Mp3Conveter** - Send a **Video** for converting to **Audio**.\n\n🎼➥ /lyric - Send me a **Song name** I give you a Lyrics.\nEg: `/lyric beggin`\n🎵➥ /s - To **download** audio songs from **YouTube**,You can use this in group.\nEg : `/s Believer`\n📹➥ /v - To **download Video** from **YouTube**, video downloading is very slowly pls wait it.\n⚫📥➥ **TikTok Download** - Send me **Tiktok** Video **Url** here\n💱➥ **G translator** - You can use me in group's in this command👉🏻 /tr first add me in group.\nClick /list to find your language.\nEg: reply to /tr en 👈🏼\n\n🆔➥ **user, group's, bot, channel's Id Finder**\n1. Send any message to get **your ID**.\n2. Forward any message from any user/bot/channel or anonymous admins to get ID.\n3. Add in group / channel to get ID.\n4. **Use /id command:**\n- in private: To get ID through username\n- in group/channel: To get ID of that chat.\n5. **Your DC**❓ - Click /dc to get your DC.\n\n🆎⍟ /about - Know me 🙋\n⍟─────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )


@Client.on_message(filters.command("about"))
async def about(bot: Client, message: Message):
    await message.reply_text(
        text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖**Mʏ Nᴀᴍᴇ:** [Tg Tool Bot](https://t.me/HTGToolBot)\n├🧑‍💻**Mʏ Dᴇᴠ:** [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢**Cʜᴀɴɴᴇʟ:** [TGG](https://t.me/Tg_Galaxy)\n├👥**Gʀᴏᴜᴘ:** [MG](https://t.me/Music_Galaxy_Dl)\n├📡**Sᴇʀᴠᴇʀ:** [Heroku](https://Heroku.com)\n├🔣**Language:** [Python](https://python.org/)\n╰───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# Sticker id

@Client.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is👇\n\n* `{message.sticker.file_id}` *", quote=True)


# Service clear

@Client.on_message(filters.service)
async def delete(bot,message):
 await message.delete()


# Telegraph

@Client.on_message(filters.private & filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"𝗢𝗼𝗽𝘀 𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝗪𝗲𝗻𝘁 𝗪𝗿𝗼𝗻𝗴\n{error} Contact @HydraLivegrambot")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass



#  Lyrics

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
**Lyrics Search Powered By Tg Tool Bot**
**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}
**__Lyrics:__**
{S.lyrics}"""
    await m.edit(xxx)

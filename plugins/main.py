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
        text="╭───────────────⍟\n│Hᴇʏ bro👋😄\n│I ᴀᴍ HʏDʀɪx's test Tool Bot[🛠️](https://telegra.ph/file/fcf03969d2344d1a62d64.jpg)\n│Click /help to know my Commands and my uses ℹ️\n╰──────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/HydrixToolsbot?startgroup=botstart")
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
        text="⍟─────[COM]─────⍟\nI Have some cool futures, More features Soon..😌\n\n🖼️⍟ **Sticker ID**❓- Just send me the Sticker I would reply with it's Id.\n👁️‍🗨️⍟ **Join Left Hider** - I Can Delete A Member joined Message,add me your group and promote.\n📜⍟ **Telegraph Uploader** - Send me any Photo I'll Upload it into Telegra.ph\n🎼⍟ /lyric - Send me a Song name I give you a Lyrics.Eg: `/lyric` <Song Name>\n📟⍟ /calculate - 👈🏼 Send me the command and type your Number to calculate.\n🔎⍟ You Can search YouTube videos in nline Mode | copy this and paste it `@HydrixToolsbot`\n🎵⍟ /s - To download audio songs from YouTube.\nEg : `/s Believer`\n\n🆎⍟ /about - Know me 🙋\n⍟─────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )


@Client.on_message(filters.command("about"))
async def about(bot: Client, message: Message):
    await message.reply_text(
        text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖**Mʏ Nᴀᴍᴇ:** [Hʏᴅʀɪx Tool Bot](https://t.me/HydrixToolsbot)\n├🧑‍💻**Mʏ Dᴇᴠ:** [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢**Cʜᴀɴɴᴇʟ:** [TGG](https://t.me/Tg_Galaxy)\n├👥**Gʀᴏᴜᴘ:** [MG](https://t.me/Music_Galaxy_Dl)\n├📡**Sᴇʀᴠᴇʀ:** [Heroku](https://Heroku.com)\n├🔣**Language:** [Python](https://python.org/)\n╰───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# Sticker id

@Client.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is👇\n\n* `{message.sticker.file_id}` *", quote=True)

# join left Hider

@Client.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
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
**Lyrics Search Powered By HyDrix Tool**
**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}
**__Lyrics:__**
{S.lyrics}"""
    await m.edit(xxx)


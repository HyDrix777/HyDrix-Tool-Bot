import os
from pyrogram import Client, filters
from pyrogram.types import *
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
        sticker="CAACAgQAAxkBAAIJrmIDj4ocjNPfq9MombsQ1EtlkviJAALeAQACS2nuEPD9ItKxUKZpHgQ"             
    )


    await message.reply_text(
        text=f"✨**Wᴇʟᴄᴏᴍᴇ** {message.from_user.mention} \n💭I ᴀᴍ **ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ**[🛠️](https://telegra.ph/file/738a362ee817361bbacd6.jpg)\n\n💡 Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
           ],[
           InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ],[
           InlineKeyboardButton(text="🔎 sᴇᴀʀᴄʜ ʏᴛ", switch_inline_query_current_chat=""),
           InlineKeyboardButton("🆎 ᴀʙᴏᴜᴛ", callback_data="about")
           ],[
           InlineKeyboardButton("🏃 ᴇxɪᴛ", url="https://t.me/MusicdGalabfdbxy_Dl")
           ]]
           )
       )

# Callback----------------

@Client.on_callback_query()
async def hydrix(bot, msg: CallbackQuery):
    if msg.data == "start":
        await msg.message.edit(
            text ="""Hello"""
        )

    elif msg.data == "about":
        await msg.message.edit(
            text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖**Mʏ Nᴀᴍᴇ:** [Tg Tool Bot](https://t.me/HTGToolBot)\n├🧑‍💻**Mʏ Dᴇᴠ:** [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢**Cʜᴀɴɴᴇʟ:** [TGG](https://t.me/Tg_Galaxy)\n├👥 **Gʀᴏᴜᴘ:** [MG](https://t.me/Music_Galaxy_Dl)\n├📡**Sᴇʀᴠᴇʀ:** [Heroku](https://Heroku.com)\n├🔣**Language:** [Python](https://python.org/)\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start")
               ]]
            )
        )

    elif msg.data == "start":
        await msg.message.edit(
            text=f"⍟─────[ᴄᴏᴍᴍ]─────⍟\nHello {msg.from_user.mention} Theis are my help session.\n\n🖼️➥ **sᴛɪᴄᴋᴇʀ ɪᴅ**❓- Just send me the Sticker I would reply with it's Id.\n[🗑](https://telegra.ph/file/9eeb97b97cc859855bfc0.jpg)➥ **ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ** - I Can Delete A Service message like join left and more,add me your group and promote it.\n📜➥ **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ** - Send me any Photo I'll Upload it into Telegra.ph\n🔎➥ /search - search YouTube videos\nEg : `/search Alen Walker`\n🔰➥ /json - Reply To Any Message To Get Json\n📹➥🎵⍟ **Mp4 to Mp3Conveter** - Send a Video for converting to Audio.\n\n🎼➥ /lyric - Send me a Song name I give you a Lyrics.\nEg: `/lyric beggin`\n🎵➥ /s - To download audio songs from YouTube,You can use this in group.\nEg : `/s Believer`\n📹➥ /v - To download Video from YouTube, video downloading is very slowly pls wait it.\n💱➥ **Gᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ** - You can use me in group's in this command👉🏻 /tr first add me in group.\nClick /list to find your language.\nEg: reply to /tr en 👈🏼\n🕹️➥ **ғᴜɴ** - Click /fun to get fun commands\n\n🆔➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ Fɪɴᴅᴇʀ**\n1. Send any message to get your ID.\n2. Forward any message from any user/bot/channel or anonymous admins to get ID.\n3. Add in group / channel to get ID.\n4. Use /id command:\n- in private: To get ID through username\n- in group/channel: To get ID of that chat.\n5. Your DC❓ - Click /dc to get your DC.\n\n🆎 /about - **Know me** 🙋\n⍟─────────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start")
               ]]
            )
        )

    elif msg.data == "help":
        await msg.message.edit(
            text="I Can Guide You Through All Of Hydrix Tools bot Cool Features And How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("Sticker", callback_data="stck"),
               InlineKeyboardButton("Clean SM", callback_data="clsm"),
               InlineKeyboardButton("Telegraph Up", callback_data="tgph")
               ],[
               InlineKeyboardButton("Search Yt", callback_data="srch"),
               InlineKeyboardButton("Jason", callback_data="jsn"),
               InlineKeyboardButton("Mp4toMp3", callback_data="conv")
               ],[
               InlineKeyboardButton("Lyrics", callback_data="lyrc"),
               InlineKeyboardButton("Song Dl", callback_data="sdl"),
               InlineKeyboardButton("Video Dl", callback_data="vdl")
               ],[
               InlineKeyboardButton("GTranslator", callback_data="gtra"),
               InlineKeyboardButton("Fun", callback_data="Fns"),
               InlineKeyboardButton("ID's", callback_data="ids")
               ]]
            )
        )

# Fun commands-------

@Client.on_message(filters.command("fun"))
async def fun(bot: Client, message: Message):
    await message.reply_text(
        text="⍟────Fun────⍟\n🔻**Here is the help for the Fun module**:\n➥ /roll : Roll a dice\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n➥ /run : reply a random string from an array of replie.\n➥ /lnm : find your lucky number.\n ➥ /love : Love 😘\n➥ /toss : Tosses A coin\n➥ /shrug : get shrug XD\n➥ /table : get flip/unflip :v\n➥ /decide : \Randomly answers yes/no/maybe.\n⍟───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# G Translator Language code list

@Client.on_message(filters.command("list"))
async def list(bot: Client, message: Message):
    await message.reply_text(
        text="⍟────[ʟɪsᴛ]────⍟\n**List is in the form**\n__Language code => Language__\n\n`af` -> Afrikaans\n`sq` -> Albanian\n`am` -> Amharic\n`ar` -> Arabic\n`hy` -> Armenian\n`az` -> Azerbaijani\n`eu` -> Basque\n`be` -> Belarusian\n`bn` -> Bengali\n`bs` -> Bosnian\n`bg` -> Bulgarian\n`ca` -> Catalan\n`ceb` -> Cebuano\n`ny` -> Chichewa\n`zh`-`cn` -> Chinese\n`co` -> Corsican\n`hr` -> Croatian\n`cs` -> Czech\n`da` -> Danish\n`nl` -> Dutch\n`en` -> English\n`eo` -> Esperanto\n`et` -> Estonian\n`tl` -> Filipino\n`fi` -> Finnish\n`fr` -> French\n`fy` -> Frisian\n`gl` -> Galician\n`ka` -> Georgian\n`de` -> German\n`el` -> Greek\n`gu` -> Gujarati\n`ht` -> Haitian creole\n`ha` -> Hausa\n`haw` -> Hawaiian\n`iw` -> Hebrew\n`hi` -> Hindi\n`hmn` -> Hmong\n`hu` -> Hungarian\n`is` -> Icelandic\n`ig` -> Igbo\n`id` -> Indonesian\n`ga` -> Irish\n`it` -> Italian\n`ja` -> Japanese*\n`jw` -> Javanese\n`kn` -> Kannada\n`kk` -> Kazakh\n`km` -> Khmer\n`rw` -> Kinyarwanda\n`ko` -> Korean\n`ku` -> Kurdish (kurmanji)\n`ky` -> Kyrgyz\n`lo` -> Lao\n`la` -> Latin\n`lv` -> Latvian\n`lt` -> Lithuanian\n`lb` -> Luxembourgish\n`mk` -> Macedonian\n`mg` -> Malagasy\n`ms` -> Malay\n`ml` -> Malayalam\n`mt` -> Maltese\n`mi` -> Maori\n`mr` -> Marathi\n`mn` -> Mongolian\n`my` -> Myanmar\n`ne` -> Nepali\n`no` -> Norwegian\n`or` -> Oriya\n`ps` -> Pashto\n`fa` -> Persian\n`pl` -> Polish\n`pt` -> Portuguese\n`pa` -> Punjabi\n`ro` -> Romanian\n`ru` -> Russian\n`sm` -> Samoan*\n`gd` -> Scots gaelic\n`sr` -> Serbian\n`st` -> Sesotho\n`sn` -> Shona\n`sd` -> Sindhi\n`si` -> Sinhala\n`sk` -> Slovak\n`sl` -> Slovenian\n`so` -> Somali\n`es` -> Spanish\n`su` -> Sundanese\n`sw` -> Swahili\n`sv` -> Swedish\n`tg` -> Tajik\n`ta` -> Tamil\n`tt` -> Tatar\n`te` -> Telugu\n`th` -> Thai\n`tr` -> Turkish\n`tk` -> Turkmen\n`ug` -> Uighur\n`uk` -> Ukrainian\n`ur` -> Urdu\n`uz` -> Uzbek\n`vi` -> Vietnamese\n`cy` -> Welsh\n`xh` -> Xhosa\n`yi` -> Yiddish\n`yo` -> Yoruba\n`zu` -> Zulu \n\n⍟───────────⍟",
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

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
        text="╭─────────────⍟\n│Hᴇʏ 🧞\n│I ᴀᴍ ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ[🛠️](https://telegra.ph/file/dad7f5c9f7572ac3cb5e1.jpg)\n│ɪ ʜᴀᴠᴇ sᴏᴍᴇ ᴄᴏᴏʟ ғᴜᴛᴜʀᴇs✨\n│ᴄʟɪᴄᴋ /help ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs\n│ᴀɴᴅ ᴍʏ ᴜsᴇs 🍃\n╰──────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
           ],[
           InlineKeyboardButton("📢 ᴄʜᴀɴɴᴇʟ", url="https://t.me/Tg_galaxy"),
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ],[
           InlineKeyboardButton(text="🔎 sᴇᴀʀᴄʜ ʏᴛ", switch_inline_query_current_chat=""),
           InlineKeyboardButton("🧑‍💻 ʙᴏᴛ ᴅᴇᴠ", url="https://t.me/Hydrix777")
           ],[
           InlineKeyboardButton("❌ ᴇxɪᴛ ❌", url="https://t.me/Musieuejedjdjaxy_Dl")
           ]]
           )
       )

@Client.on_message(filters.private & filters.command("help"))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text="⍟─────[ᴄᴏᴍᴍ]─────⍟\n🔻ᴍʏ ғᴜᴛᴜʀᴇ's🔻\n\n🖼️➥ **sᴛɪᴄᴋᴇʀ ɪᴅ**❓- Just send me the Sticker I would reply with it's Id.\n🗑➥ **ᴄʟᴇᴀɴ ᴇᴠᴇɴᴛs** - I Can Delete A **Service message** like join left and more,add me your group and promote it.\n📜➥ **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ** - Send me any **Photo** I'll Upload it into Telegra.ph\n🔎➥ You Can search **ʏᴏᴜᴛᴜʙᴇ** videos in **ɴʟɪɴᴇ ᴍᴏᴅᴇ** | copy this and paste it `@HTGToolBot`\n📹➥🎵⍟ **ᴍᴘ𝟺** Tᴏ **ᴍᴘ𝟹ᴄᴏɴᴠᴇᴛᴇʀ** - Send a **Video** for converting to **Audio**.\n\n🎼➥ /lyric - Send me a **Song name** I give you a Lyrics.\nEg: `/lyric beggin`\n🎵➥ /s - To **download** audio songs from **ʏᴏᴜᴛᴜʙᴇ**,You can use this in group.\nEg : `/s Believer`\n📹➥ /v - To **download Video** from **ʏᴏᴜᴛᴜʙᴇ**, video downloading is very slowly pls wait it.\n⚫➥ **ᴛɪᴋᴛᴏᴋ ᴅᴏᴡɴʟᴏᴀᴅ** - Send me **Tiktok** Video **Url** here\n💱➥ **ɢ ᴛʀᴀɴsʟᴀᴛᴏʀ** - You can use me in group's in this command👉🏻 /tr first add me in group.\nClick /list to find your language.\nEg: reply to /tr en 👈🏼\n🕹️➥ **ғᴜɴ** - Click /fun to get fun commands\n\n🆔➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, ʙᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ ғɪɴᴅᴇʀ**\n1. Send any message to get **your ID**.\n2. Forward any message from any user/bot/channel or anonymous admins to get ID.\n3. Add in group / channel to get ID.\n4. **Use /id command:**\n- in private: To get ID through username\n- in group/channel: To get ID of that chat.\n5. **Your DC**❓ - Click /dc to get your DC.\n\n🆎⍟ /about - Know me 🙋\n⍟─────────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# G Translator Language code list

@Client.on_message(filters.command("list"))
async def list(bot: Client, message: Message):
    await message.reply_text(
        text="⍟────[ʟɪsᴛ]────⍟\n`ʟɪsᴛ ɪs ɪɴ ᴛʜᴇ ғᴏʀᴍ`\n**Language code** => **Language**\n\n`af` ➥ **Afrikaans**\n`sq` -> **Albanian**\n`am` -> **Amharic**\n`ar` -> **Arabic**\n`hy` -> **Armenian**\n`az` -> **Azerbaijani**\n`eu` -> **Basque**\n`be` -> **Belarusian**\n`bn` -> **Bengali**\n`bs` -> **Bosnian**\n`bg` -> **Bulgarian**\n`ca` -> **Catalan**\n`ceb` -> **Cebuano**\n`ny` -> **Chichewa**\n`zh`-`cn` -> **Chinese**\n`co` -> **Corsican**\n`hr` -> **Croatian**\n`cs` -> **Czech**\n`da` -> **Danish**\n`nl` -> **Dutch**\n`en` -> **English**\n`eo` -> **Esperanto**\n`et` -> **Estonian**\n`tl` -> **Filipino**\n`fi` -> **Finnish**\n`fr` -> **French**\n`fy` -> **Frisian**\n`gl` -> **Galician**\n`ka` -> **Georgian**\n`de` -> **German**\n`el` -> **Greek**\n`gu` -> **Gujarati**\n`ht` -> **Haitian creole**\n`ha` -> **Hausa**\n`haw` -> **Hawaiian**\n`iw` -> **Hebrew**\n`hi` -> **Hindi**\n`hmn` -> **Hmong**\n`hu` -> **Hungarian**\n`is` -> **Icelandic**\n`is` -> **Icelandic**\n`ig` -> **Igbo**\n`id` -> **Indonesian**\n`ga` -> **Irish**\n`it` -> **Italian**\n`ja` -> **Japanese*\n`jw` -> **Javanese**\n`kn` -> **Kannada**\n`kk` -> **Kazakh**\n`km` -> **Khmer**\n`rw` -> **Kinyarwanda**\n`ko` -> **Korean**\n`ku` -> **Kurdish (kurmanji)**\n`ky` -> **Kyrgyz**\n`lo` -> **Lao**\n`la` -> **Latin**\n`lv` -> **Latvian**\n`lt` -> **Lithuanian**\n`lb` -> **Luxembourgish**\n`mk` -> **Macedonian**\n`mg` -> **Malagasy**\n`ms` -> **Malay**\n`ml` -> **Malayalam**\n`mt` -> **Maltese**\n`mi` -> **Maori**\n`mr` -> **Marathi**\n`mn` -> **Mongolian**\n`my` -> **Myanmar**\n`ne` -> **Nepali**\n`no` -> **Norwegian**\n`or` -> **Oriya**\n`ps` -> **Pashto**\n`fa` -> **Persian**\n`pl` -> **Polish**\n`pt` -> **Portuguese**\n`pa` -> **Punjabi**\n`ro` -> **Romanian**\n`ru` -> **Russian**\n`sm` -> **Samoan*\n`gd` -> **Scots gaelic**\n`sr` -> **Serbian**\n`st` -> **Sesotho**\n`sn` -> **Shona**\n`sd` -> **Sindhi**\n`si` -> **Sinhala**\n`sk` -> **Slovak**\n`sl` -> **Slovenian**\n`so` -> **Somali**\n`es` -> **Spanish**\n`su` -> **Sundanese**\n`sw` -> **Swahili**\n`sv` -> **Swedish**\n`tg` -> **Tajik**\n`ta` -> **Tamil**\n`tt` -> **Tatar**\n`te` -> **Telugu**\n`th` -> **Thai**\n`tr` -> **Turkish**\n`tk` -> **Turkmen**\n`ug` -> **Uighur**\n`uk` -> **Ukrainian**\n`ur` -> **Urdu**\n`uz` -> **Uzbek**\n`vi` -> **Vietnamese**\n`cy` -> **Welsh**\n`xh -> **Xhosa**\n`yi` -> **Yiddish**\n`yo` -> **Yoruba**\n`zu` -> **Zulu** \n\n⍟───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# Fun Comm------

@Client.on_message(filters.command("fun"))
async def fun(bot: Client, message: Message):
    await message.reply_text(
        text="⍟─────[ғᴜɴ]─────⍟\n🔻**Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ ғᴜɴ ᴍᴏᴅᴜʟᴇ**:\n➥ /roll : Roll a dice\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n➥ /run : reply a random string from an array of replie.\n➥ /lnm : find your lucky number.\n ➥ /love : Love 😘\n➥ /toss : Tosses A coin\n➥ /shrug : get shrug XD\n➥ /table : get flip/unflip :v\n➥ /decide : \Randomly answers yes/no/maybe.\n⍟───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# About

@Client.on_message(filters.private & filters.command("about"))
async def about(bot: Client, message: Message):
    await message.reply_text(
        text="╭────[ᴀʙᴏᴜᴛ]────⍟\n├🤖**ᴍʏ ɴᴀᴍᴇ:** [ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ](https://t.me/HTGToolBot)\n├🧑‍💻**ᴍʏ ᴅᴇᴠ:** [Hʏᴅʀɪx](https://t.me/Hydrix777)\n├📢**ᴄʜᴀɴɴᴇʟ:** [ᴛɢɢ](https://t.me/Tg_Galaxy)\n├👥**ɢʀᴏᴜᴘ:** [ᴍɢ](https://t.me/Music_Galaxy_Dl)\n├📡**sᴇʀᴠᴇʀ:** [ʜᴇʀᴏᴋᴜ](https://Heroku.com)\n├🔣**ʟᴀɴɢᴜᴀɢᴇ:** [ᴘʏᴛʜᴏɴ](https://python.org/)\n╰───────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

# Sticker id

@Client.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ sᴛɪᴄᴋᴇʀ's ɪᴅ ɪs👇\n\n* `{message.sticker.file_id}` *", quote=True)


# Service clear

@Client.on_message(filters.group & filters.service)
async def delete_events(bot, msg):
    try:
        chat_member = await bot.get_chat_member(msg.chat.id, "self")
    except Exception:  # Like kicked, etc.
        return
    if chat_member.status == "administrator":
        if chat_member.can_delete_messages:
            await msg.delete()
        else:
            await msg.reply(
                "I'm surely admin, but I don't have 'Delete Messages' permission !!!"
            )
    else:
        await msg.reply(
            "I'm not admin, so I can't delete messages. \n\nMake me admin or kick me outta here."
        )

# Telegraph

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
        await dwn.edit_text(f"Oᴏᴘs sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ\n{error} ᴄᴏɴᴛᴀᴄᴛ @HydraLivegrambot")
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

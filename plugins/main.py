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
                f"#NEWUSER: \n\nNew User [{message.from_user.mention}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.mention}\n ID : {message.from_user.id}")
    await message.reply_sticker(
        sticker="CAACAgIAAxkBAAIupmJOkAXmE1GMXhehhHk2_WHHC0ayAALTAANWnb0K9TKPl9US-T0eBA"             
    )

    await message.reply_text(
        text=f"✨ **ʜᴇʏ** ||{message.from_user.mention}||!\n\n💭 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ **ʜʏᴅʀɪx** ᴛᴏᴏʟs ʙᴏᴛ [🛠️](https://telegra.ph/file/f1ba9b8c2ce7e659e51f6.mp4)\n ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ʜᴇʟᴘғᴜʟʟ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴍʏ ᴘᴍ\n\n💡 ʜɪᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛᴏ ᴍʏ ғᴜʟʟ ᴍᴏᴅᴜʟᴇs\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!\n\nᴛʜɪs ʙᴏᴛ ᴍᴀɪɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴍʏ **ᴏᴡɴᴇʀ**❗",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("✨ ᴀʙᴏᴜᴛ", callback_data="about")
           ],[
           InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀᴛ!", url="http://t.me/HTGToolBot?startgroup=botstart"),
           InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/songdownload_group")
           ],[
           InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")
           ],[
           InlineKeyboardButton("🤖 ᴍʏ ʙᴏᴛ's", callback_data="bots"),
           InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete")
           ]]
           )
       )


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


@Client.on_message(filters.private & filters.command("stat"))
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

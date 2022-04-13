from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio




# Callback---------------

@Client.on_callback_query()
async def hydrix(bot, msg: CallbackQuery):
    if msg.data == "start":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(9.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(9.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(9.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(9.5)

        await reply4.delete()

        await msg.message.edit(
            text =f"""Sooon....🙄||{msg.from_user.first_name}😁||"""
        )

    elif msg.data == "srrt":

        await msg.message.reply_chat_action("Typing")
        await asyncio.sleep(1)

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)
        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)
        await reply4.delete() 


        await msg.message.edit(
            text=f"✨ ʜᴇʟʟᴏ {msg.from_user.mention} !\n\n💭 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ **ʜʏᴅʀɪx** ᴛᴏᴏʟs ʙᴏᴛ [🛠️](https://telegra.ph/file/f1ba9b8c2ce7e659e51f6.mp4)\n ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ʜᴇʟᴘғᴜʟʟ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴍʏ ᴘᴍ\n\n💡 ʜɪᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛᴏ ᴍʏ ғᴜʟʟ ᴍᴏᴅᴜʟᴇs\nʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚\nCᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!\n\nᴛʜɪs ʙᴏᴛ ᴍᴀɪɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴍʏ **ᴏᴡɴᴇʀ**❗",
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕", url="http://t.me/HTGToolBot?startgroup=botstart")
               ],[
               InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
               InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/songdownload_group")
               ],[
               InlineKeyboardButton("🆎 ᴀʙᴏᴜᴛ", callback_data="about")
               ],[
               InlineKeyboardButton("🤖 ᴍʏ ʙᴏᴛ's", callback_data="bots"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete")
               ]]
            )
        )
               
    elif msg.data == "about":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="╭───[•](https://telegra.ph/file/65005f9a58ca27140cdc0.jpg)[ᴀʙᴏᴜᴛ]\n│➪ **ᴍʏ ɴᴀᴍᴇ**: [ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ](https://t.me/HTGToolBot)\n│➪ **ᴄʀᴇᴀᴛᴏʀ**: [ʜʏᴅʀɪx](https://t.me/HydraLivegrambot)\n│➪ **ᴄʜᴀɴɴᴇʟ**: [ᴛɢɢ](https://t.me/Tg_Galaxy)\n│➪ **ɢʀᴏᴜᴘ**: [ᴍɢ](https://t.me/songdownload_group)\n│➪ **sᴇʀᴠᴇʀ**: [ʜᴇʀᴏᴋᴜ](https://Heroku.com)\n│➪ **ʟɪʙʀᴀʀʏ**: [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org/)\n│➪ **ʟᴀɴɢᴜᴀɢᴇ**: [ᴘʏᴛʜᴏɴ 𝟹](https://python.org/)\n│➪ **ᴅᴀᴛᴀʙᴀsᴇ**: [ᴍᴀɴɢᴏ ᴅʙ](https://mongodb.com)\n│➪ **ʙᴜɪʟᴅ sᴛᴀᴛᴜs**: `v4.0.1 [ʙᴇᴛᴀ]`\n╰───────────⍟",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete")
               ]]
            )
        )

    elif msg.data == "help":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention} ᴍʏ ɴᴀᴍᴇ ɪs ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ.\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg) __ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\nMore Coming Soon ....",
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
               InlineKeyboardButton("ɪᴅ&ɪɴғᴏ", callback_data="ids")
               ],[
               InlineKeyboardButton("ʏᴛ ᴛʜᴜᴍʙ ᴅʟ", callback_data="ytthumb"),
               InlineKeyboardButton("ᴘᴀsᴛᴇ", callback_data="past"),
               InlineKeyboardButton("ᴛᴛs", callback_data="tts")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete"),
               InlineKeyboardButton("ɴᴇxᴛ »", callback_data="next")
               ]]
            )
        )
# Next Module2-------
    elif msg.data == "next":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention} ᴍʏ ɴᴀᴍᴇ ɪs ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ.\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg) __ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\nMore Coming Soon ....",
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
               InlineKeyboardButton("ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ", callback_data="fltv"),
               InlineKeyboardButton("ᴠɪᴅᴇᴏ𝟸-ғɪʟᴇ", callback_data="cv2f")
               ],[
               InlineKeyboardButton("ᴘɪɴɢ", callback_data="pinj"),
               InlineKeyboardButton("ᴘᴀss ɢᴇɴᴇʀᴀᴛ", callback_data="pasg"),
               InlineKeyboardButton("ɪᴍᴅʙ", callback_data="imbd")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help"),
               InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete"),
               InlineKeyboardButton("ɴᴇxᴛ »", callback_data="next2")
               ]]
            )
        )
# Next Module3-------
    elif msg.data == "next2":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention} ᴍʏ ɴᴀᴍᴇ ɪs ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ.\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg) __ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\nMore Coming Soon ....",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("sᴛʏʟɪsʜ ᴛxᴛ", callback_data="styl"),
               InlineKeyboardButton("ʜᴀɴᴅᴡʀɪᴛ", callback_data="hand"),
               InlineKeyboardButton("ᴀʟɪᴠᴇ", callback_data="aliv")
               ],[
               InlineKeyboardButton("ᴘᴅғ ᴛᴏ ᴛᴇxᴛ", callback_data="pdft"),
               InlineKeyboardButton("ᴀᴜᴅɪᴏʙᴏᴏᴋ", callback_data="audi"),
               InlineKeyboardButton("ᴄᴀʀʙᴏɴ", callback_data="crbn")
               ],[
               InlineKeyboardButton("ɴᴏ ʟɪɴᴋ's", callback_data="nlng"),
               InlineKeyboardButton("ᴍᴜsɪᴄ ᴛᴀɢ", callback_data="must"),
               InlineKeyboardButton("sᴛɪᴋʀ ᴛᴏ ɪᴍɢ", callback_data="stki")
               ],[
               InlineKeyboardButton("sʜᴀʀᴇ", callback_data="shar"),
               InlineKeyboardButton("ᴜʀʟ sʜᴏʀᴛ", callback_data="urls"),
               InlineKeyboardButton("ᴛᴀɢ ᴀʟʟ", callback_data="taga")
               ],[
               InlineKeyboardButton("ᴡᴇʙ-sᴄʀᴀᴘᴘᴇʀ", callback_data="wpsp"),
               InlineKeyboardButton("ᴜɴᴢɪᴘᴇʀ", callback_data="unzp"),
               InlineKeyboardButton("ʀᴇɴᴀᴍᴇʀ", callback_data="rnmr")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next"),
               InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete"),
               InlineKeyboardButton("ɴᴇxᴛ »", callback_data="next3")
               ]]
            )
        )
# Next Module4-------
    elif msg.data == "next3":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention} ᴍʏ ɴᴀᴍᴇ ɪs ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ,\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg) __ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\n__This is a group manager module__\nthere some module are not working 🙂",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("ᴜɴʟɪᴍɪᴛᴇᴅ ғɪʟᴛᴇʀ", callback_data="unfl"),
               InlineKeyboardButton("ᴘᴜʀɢᴇs", callback_data="purg"),
               InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", callback_data="repo")
               ],[
               InlineKeyboardButton("ᴘɪɴ", callback_data="pins"),
               InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="mute"),
               InlineKeyboardButton("ᴢᴏᴍʙɪᴇs", callback_data="zomb")
               ],[
               InlineKeyboardButton("ᴡᴀʀɴs", callback_data="warn"),
               InlineKeyboardButton("ɢʀᴇᴇᴛɪɴɢs", callback_data="wlcm"),
               InlineKeyboardButton("ʟᴏᴄᴋs", callback_data="lock")
               ],[
               InlineKeyboardButton("ᴀᴘᴘʀᴏᴠᴀʟ", callback_data="aprl"),
               InlineKeyboardButton("ɴᴏᴛᴇs", callback_data="note"),
               InlineKeyboardButton("ʀᴜʟᴇs", callback_data="rule")
               ],[
               InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="admi"),
               InlineKeyboardButton("ʙᴀɴs", callback_data="bans"),
               InlineKeyboardButton("ғɪʟᴛᴇʀs", callback_data="fltr")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2"),
               InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete"),
               InlineKeyboardButton("ɴᴇxᴛ »", callback_data="next4")
               ]]
            )
        )

# Next Module5-------
    elif msg.data == "next4":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text=f"ʜᴇʏ {msg.from_user.mention} ᴍʏ ɴᴀᴍᴇ ɪs ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ.\n\n[🔰](https://telegra.ph/file/73669866e33d8be72033b.jpg) __ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.__\n\nMore Coming Soon ....",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("ɢᴏ-ғɪʟᴇ", callback_data="gofl"),
               InlineKeyboardButton("ᴀɴᴏɴғɪʟᴇs", callback_data="anfl"),
               InlineKeyboardButton("soon", callback_data="start")
               ],[
               InlineKeyboardButton("sOon", callback_data="start"),
               InlineKeyboardButton("soon", callback_data="start"),
               InlineKeyboardButton("soon", callback_data="start")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3"),
               InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete"),
               InlineKeyboardButton("ɴᴇxᴛ »", callback_data="start")
               ]]
            )
        )

# futures------
    elif msg.data == "stck":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[📚](https://telegra.ph/file/4080224664799812688b6.jpg) **sᴛɪᴄᴋᴇʀ ɪᴅ ᴄᴏᴍᴍᴀɴᴅs**\n\n➪ __ʜᴇʀ ɪs sɪᴍᴘʟᴇ **sᴛɪᴄᴋᴇʀ ɪᴅ** ᴍᴏᴅᴜʟᴇ ғᴏʀ ʏᴏᴜ, ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ ғʀᴏᴍ ʜᴇʀᴇ.__\nғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ **sᴛɪᴄᴋᴇʀ** , ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴅᴏᴡɴ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅ.\n\n**ᴇxᴀᴍᴘʟᴇ:**\n- `/stickerid` : ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "clsm":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🗑️](https://telegra.ph/file/c311d906b5bb2db7cf03e.jpg) **ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ**\n\n➪ __ᴅᴇʟᴇᴛᴇ ᴀʟʟ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇs. ᴛʜᴏsᴇ ᴀʀᴇ ᴛʜᴇ ᴀɴɴᴏʏɪɴɢ 'x ᴊᴏɪɴᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ' ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs ʏᴏᴜ sᴇᴇ ᴡʜᴇɴ ᴘᴇᴏᴘʟᴇ ᴊᴏɪɴ.__\n__ɪ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ᴀ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ʟɪᴋᴇ ᴊᴏɪɴ ʟᴇғᴛ ᴀɴᴅ ᴍᴏʀᴇ,ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ɪᴛ.__\n\n**ᴇxᴀᴍᴘʟᴇ:**\n- `/cleanservice` [ᴏɴ ᴏʀ ᴏғғ] : ᴛᴜʀɴ ᴏɴ ᴏʀ ᴏғғ ᴛʜᴇ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ᴄʟᴇᴀɴᴇʀ.\n- `/cleanservice on` : **ᴏɴ** ᴛʜᴇ ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘ.\n- `/cleanservice off` : **ᴏғғ** ᴛʜᴇ ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘ.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "tgph":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[📜](https://telegra.ph/file/d1d7357dc98aeb2253c2a.jpg) **ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ**\n\n➪ __ᴛʜɪs ɪs ᴀ **ᴛᴇʟᴇɢʀᴀᴘʜ** ᴜᴘʟᴏᴀᴅᴇʀ ᴍᴏᴅᴜʟᴇ, sᴇɴᴅ ᴍᴇ ᴜɴᴅᴇʀ 𝟻ᴍʙ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ, ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ I'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ɪɴᴛᴏ__ telegra.ph\nᴠɪᴅᴇᴏ ᴜᴘʟᴏᴀᴅᴇ ɴᴏᴛ sᴏᴘᴘᴏʀᴛ\n\n**ᴇxᴀᴍᴘʟᴇ:**\n- `/tgraph` : ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ ᴇᴛᴄ.\n- `/telegraph` : ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ ᴇᴛᴄ.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "srch":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔎 **Search YouTube videos**\n\n📚 **Available Commands**\n\n➥ /ytsearch - __search **YouTube** videos__\n\nEg : `/ytsearch Alen Walker`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "jsn":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📚 **Available Command**\n\n[📑](https://telegra.ph/file/d0717d29431518ff9dc21.jpg)➥ /json - __Reply To Any Message To Get Json__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "conv":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[📹](https://telegra.ph/file/5489b184451feaf8411d0.jpg)➋🎵➥ **Video to Mp3Conveter**\n__Send a Video for converting to Audio.__\n\n📚 **Available Commands**\n\nFirst send me the video file,\n/convertaudio - 👈🏼 Reply to video file then im Convert to audio.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "lyrc":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🎼](https://telegra.ph/file/12155873bb98142cc2759.jpg) Here is the help for **Lyrics Download:**\n\n📚 **Available Commands**\n\n➥ /lyric - __[Music Name] Searches Lyrics for the particular Music on web.__\n\nEg: `/lyric beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "sdl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🎵](https://telegra.ph/file/83ece4c8a4764fac97c4d.jpg) Here is the help for **Music Download**:\n\n📚 **Available Commands**\n\n➥ /s - __To download audio songs from YouTube, This only work in my PM.__\n/song - __use this command to fast download songs from YouTube__\n\nEg: `/s beggin`\n`/song beggin`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "vdl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[📹](https://telegra.ph/file/341e13067287db1b820d7.jpg) **Vedio download**\n\n__You can use this command for download videos from youtube__\n\n📚 **Available Command**\n\n➥ /v - __To download Video from YouTube, video downloading is very slowly pls wait it.__\n/video - __use this command to fast download videos from YouTube__\n\nEg: `/v alone`\n`/video alone`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "gtra":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[💱](https://telegra.ph/file/e655830a9d113c27a28ee.jpg)➥ **Google Translator Bot**\n\n__**Google Translator** which means , A bot to help you translate text to few Languages from any other language in world.__\n\n__Google Translator bot is able to detect a wide variety of languages because he is a grand son of Google Translate API.__\n\n__You can use Google Translator in his private chat & Groups.__\n\n**How To Use**\n\n➥ /tr (language code) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs or my pm\n➥ 👇🏼Click **lang list** __botton to find your language code__.👇🏼",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help"),
               InlineKeyboardButton("📜 ʟᴀɴɢ ʟɪsᴛ", callback_data="lagl")
               ]]
            )
        )
    elif msg.data == "lagl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="────[ʟɪsᴛ]────\n**List is in the form**\n__Language code => Language__\n\n`af` -> Afrikaans\n`sq` -> Albanian\n`am` -> Amharic\n`ar` -> Arabic\n`hy` -> Armenian\n`az` -> Azerbaijani\n`eu` -> Basque\n`be` -> Belarusian\n`bn` -> Bengali\n`bs` -> Bosnian\n`bg` -> Bulgarian\n`ca` -> Catalan\n`ceb` -> Cebuano\n`ny` -> Chichewa\n`zh`-`cn` -> Chinese\n`co` -> Corsican\n`hr` -> Croatian\n`cs` -> Czech\n`da` -> Danish\n`nl` -> Dutch\n`en` -> English\n`eo` -> Esperanto\n`et` -> Estonian\n`tl` -> Filipino\n`fi` -> Finnish\n`fr` -> French\n`fy` -> Frisian\n`gl` -> Galician\n`ka` -> Georgian\n`de` -> German\n`el` -> Greek\n`gu` -> Gujarati\n`ht` -> Haitian creole\n`ha` -> Hausa\n`haw` -> Hawaiian\n`iw` -> Hebrew\n`hi` -> Hindi\n`hmn` -> Hmong\n`hu` -> Hungarian\n`is` -> Icelandic\n`ig` -> Igbo\n`id` -> Indonesian\n`ga` -> Irish\n`it` -> Italian\n`ja` -> Japanese*\n`jw` -> Javanese\n`kn` -> Kannada\n`kk` -> Kazakh\n`km` -> Khmer\n`rw` -> Kinyarwanda\n`ko` -> Korean\n`ku` -> Kurdish (kurmanji)\n`ky` -> Kyrgyz\n`lo` -> Lao\n`la` -> Latin\n`lv` -> Latvian\n`lt` -> Lithuanian\n`lb` -> Luxembourgish\n`mk` -> Macedonian\n`mg` -> Malagasy\n`ms` -> Malay\n`ml` -> Malayalam\n`mt` -> Maltese\n`mi` -> Maori\n`mr` -> Marathi\n`mn` -> Mongolian\n`my` -> Myanmar\n`ne` -> Nepali\n`no` -> Norwegian\n`or` -> Oriya\n`ps` -> Pashto\n`fa` -> Persian\n`pl` -> Polish\n`pt` -> Portuguese\n`pa` -> Punjabi\n`ro` -> Romanian\n`ru` -> Russian\n`sm` -> Samoan*\n`gd` -> Scots gaelic\n`sr` -> Serbian\n`st` -> Sesotho\n`sn` -> Shona\n`sd` -> Sindhi\n`si` -> Sinhala\n`sk` -> Slovak\n`sl` -> Slovenian\n`so` -> Somali\n`es` -> Spanish\n`su` -> Sundanese\n`sw` -> Swahili\n`sv` -> Swedish\n`tg` -> Tajik\n`ta` -> Tamil\n`tt` -> Tatar\n`te` -> Telugu\n`th` -> Thai\n`tr` -> Turkish\n`tk` -> Turkmen\n`ug` -> Uighur\n`uk` -> Ukrainian\n`ur` -> Urdu\n`uz` -> Uzbek\n`vi` -> Vietnamese\n`cy` -> Welsh\n`xh` -> Xhosa\n`yi` -> Yiddish\n`yo` -> Yoruba\n`zu` -> Zulu \n\n───────────",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="gtra")
               ]]
            )
        )

    elif msg.data == "Fns":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🤪](https://telegra.ph/file/a3a5895a4e312e9f3d803.jpg) **Here is the help for the Fun module**:\n\n📚 **Available Commands**\n\n➥ /roll : __Roll a dice__\n➥ /ball\n➥ /pog\n➥ /throw\n➥ /goal\n➥ /luck\n➥ /slap: slap a user, or get slapped if not a reply.\n➥ /shout `<keyword>`: write anything you want to give loud shout.\n➥ /bluetext : check urself :V\n➥ /react : Random Reaction.\n\n➥ /run : __reply a random string from an array of replie.__\n➥ /runml : __reply a random string from an Malayalam lang array of replie.__ \n➥ /lnm : __find your lucky number.__\n➥ /love : __Love__ 😘\n➥ /toss : __Tosses A coin__\n➥ /shrug : __get shrug XD__\n➥ /table : __get flip/unflip__ :v\n➥ /decide : __Randomly answers yes/no/maybe__.\n➥ /truth :__asks you a question__\n➥ /tord : __can be a truth or a dare__.\n➥ /dare : __gives you a dare__\n➥ /rather : __would you rather__\n➥ /goodnight : Good night 😴\n➥ /morning : good morning 😊🌄\n➥ /abuse : labuse 🤬\n➥ /cry : Cry 😭🥲\n➥ /anime : Anime",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ids":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🆔](https://telegra.ph/file/8671a3c153c0f609dc697.jpg)➥ **ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅ Fɪɴᴅᴇʀ**\n\n📚 **Available Commands**\n\n1. __Send any message to get your ID.__\n2. __Forward any message from any user/bot/channel/group or anonymous admins to get ID.__\n3. __Add in group / channel to get ID.__\n4. Use /id command:\n- in private: To get ID through username\n- in group/channel: To get ID of that chat\n5. Your DC❓ : Click /dc to get your DC.\n6. /info : this command to get your all information, only work my Pm.\n- /ginfo : this command to get your group information ℹ️, this only work in group.\n- /id **Message ID** : just reply to any message in group to get message id\n➥ /infog & /whois - get more information about a user and group\n➥ /botstaff : only bot owner can use this command.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "past":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📇 **Paste**\n\n__Paste some texts or documents on a website!__\n\n📚 **Available Commands**\n➥ /paste [text] - Paste The Given Text On Pasty\n\n__These commands works on both pm and group.__\n__These commands can be used by any group member.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "tts":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🗣️](https://telegra.ph/file/f1cf0da2397558752fba8.jpg) **ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ** - ᴛᴛs\n\n__A Module To Convert TEXT To Voice With Language Support__\n\n📚 **Available Command**\n\n⍟ /tts : __Reply To Any TEXT message I will Convert As Audio__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )

    elif msg.data == "ytthumb":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔴 **YouTube Thumbnail Dl**\n\nsᴇɴᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.\n\n📚 **Available Commands**\n\n/ytthumb use this command to Yt link, to get thumbnail.\nExample: `/ytthumb http://www.youtube.com/watch?v=HhjHYkPQ8F0`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help")
               ]]
            )
        )


    elif msg.data == "bots":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="╭──•**Mʏ ʙᴏᴛs ʟɪsᴛ**[📋](https://telegra.ph/file/4953f6bfb4688acdf6649.jpg)\n├•**Tʜᴇɪs ᴀʀᴇ ᴍʏ ᴏᴛʜᴇʀ ʙᴏᴛs**\n│\n├•𝟙. `Stylish Text bot`\n├•𝟚. `Youtube Dl bot`\n├•𝟛. `Mention All bot`\n├•𝟜. `URL Uploader bot`\n├•𝟝. `Music Dl bot`\n├•𝟞. `Google Translator bot`\n├•𝟟. AntiChannel Ban bot\n│\n╰───────────⍟",
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
               InlineKeyboardButton("𝟟. AntiChannel Ban", url="https://t.me/AntiChannelBan_xbot")
               ],[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="srrt"),
               InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="delete")
               ]]
            )
        ) 

    elif msg.data == "gith":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🐈](https://telegra.ph/file/d428512e34fd9594ab1c3.jpg) **GitHub**\n\n📚 **Available Commands**\n\n➥ /github - Get your [GitHub](https://github.com) profile in my PM\nEg: `/github Username`",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "covi":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🌍 **Covid Information**\n\n__A Module To Find All Country Informations. Use This Module To Get Covid Informations Of All Countries__\n\n📚 **Available Commands**\n\n[🦠](https://telegra.ph/file/8dfbbf70b17e26d62b18c.jpg) ➥ /covid [country name] - __Use This Method To Get Covid Informations.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "forw":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📨 **Forward message remover**\n\n⍟ __I am automatically remove forward messages from group, add me your group and promote.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "plat":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🧩](https://telegra.ph/file/42d7e70b678f4ea03e1b5.jpg) **ᴘʟᴀʏ sᴛᴏʀᴇ**\n\n⍟ __hey this is a play store module,\n__This will Search application details of any app and give play store download link.__\n\n📚 **Available Commands**\n\nClick here /playstore 👈🏼",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "rmbg":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🎴 **ᴘʜᴏᴛᴏ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇ**\n\n⍟ __I'm photo background remover, send me the photo i will send the photo without background__.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "glit":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🥴 **ɢʟɪᴛᴄʜ ᴀʀᴛ**\n\n⍟ __This module help you photo to glitch in group,Just send me the image in Group not pm__ 😁.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "dinl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🤖 **ʀᴇᴍᴏᴠᴇ ɪɴʟɪɴᴇ ᴍᴇssᴀɢᴇ**\n\n⍟ __This module to automatically deletes Inline messages sent Through Bot in Group's__.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "shaz":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🎶](https://telegra.ph/file/d67ebb887ee63d33d970c.jpg)➥ **Shazam Music Finder**\n\n__You have a part of a song, but could not find out what that song is?__\n__Here's the best solution for you. Just send me a audio file sample and I'll tell you what is that song.__\n\n📚 **Available Commands**\n\n**Step 1** : __Send me a Audio__\n\n**Step 2** : __Reply your to Audio with this__ /audify __command__\n/audify : __Reply to Audio__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "emsa":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📝 **Edit Message Alert**\n\n__A Telegram Bot to Show alert when someone edits a message in Group__\n",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "yttf":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🏷️ **YouTube Tag Finder**\n\n__A telegram Bot That can extract any YouTube video Tag easy__\n__first give me the yt **URL**, and i extract tag for U__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "pins":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📌 **Pin**\n\n____Here you find find all help related to groups pins and how to manage them via me.\n__All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!__\n\n📚 **Available Commands**\n\n➥ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.__\n➥ /unpin : __I can Unpin the current pinned message in silently.__\n➥ /unpinall: Unpins all the pinned message in the current chat.\n➥ /pinned: Gives the current pinned message of the chat.\n➥ /cleanlinked `<on/off/yes/no>`: Toggle cleanlinked status. All the messages from linked channel will be deleted if enabled!\n➥ /permapin `<text>`: Pin a custom messages via bot. This message can contain markdown, and can be used in replies to the media include additional buttons and text.\n➥ /antichannelpin `<on/off/yes/no>`: Toggle antichannelpin status. All the messages from linked channel will be unpinned if enabled!\n",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "purg":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="❗ **Purge**\n\n__Here is the help for the **Purges** module:__\n\n📚 **Available Commands**\n\n➥ /purge: deletes all messages between this and the replied to message.\n➥ /spurge: Same as purge, but doesnt send the final confirmation message.\n➥ /del: deletes the message you replied to.\n\nExample:\n`/purge Delete all messages from the replied to message, until now.`\n- Mark the first message to purge from (as a reply).\n/purge",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "pinj":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📍 Here is the help for **Ping**:\n\n➥ /ping - __Check if Bot is alive or not.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "mute":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔕 **Mute & Unmute**\n\n__Want someone to keep quite for a while in the group?__\n__Mute plugin is here to help, mute or unmute any user easily!__\n__This module allows you to do mute & unmute in group easily, by exposing some common actions!__\n\n📚 **Available Commands**\n\n➥ /mute : Mute the user replied to or mentioned.\n➥ /unmute: Unmutes the user mentioned or replied to.\n➪ /smute: silences a user without notifying. Can also be used as a reply, muting the replied to user.\n➪  /dmute: Mute a user by reply, and delete their message.\n➥ /tmute <userhandle> x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.\n➪ /stmute <userhandle> x(m/h/d): mutes a user for x time without notifying. (via handle, or reply). m = minutes, h = hours, d = days.\n➪ /dtmute <userhandle> x(m/h/d): Mute the replied user, and delete the replied message. (via reply). m = minutes, h = hours, d = days\n\n➥ **𝖭𝗈𝗍𝖾:**\n𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.\n\n➛**𝖤𝗑𝖺𝗆𝗉𝗅𝖾:**\n/mute @username`; this mutes a user.\n/𝗍𝗆𝗎𝗍𝖾 2𝖽.\n\n`𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌`: 𝗆/𝗁/𝖽.\n • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌\n • 𝗁 = 𝗁𝗈𝗎𝗋𝗌\n • 𝖽 = 𝖽𝖺𝗒𝗌",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "imbd":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🎞️ **Movie Information**\n\n__A Module To Get The Movie Informations. Use This Module To Get Movie Informations__\n\n[📚](https://telegra.ph/file/ceb40ac901886eb603c5a.jpg) **Available Commands**\n\n➥ /imdb : __Get The Film Information From IMDB Source__\n➥ /search : __Get The Movie Information From Various Sources__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "styl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()
     
        await msg.message.edit(
            text="🖋️ **Stylish Text**\n\n__a module for stylish text__\n__i can help you to get stylish fonts.__\n__just send me the some text & Reply to a text message to make stylish Text.__\n\n📚 **Available Commands**\n\n➥ /text : __Reply to a text message as to make S Text__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "hand":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🖊️ **Handwriting**\n\n📚 **Available Commands**\n➥ /h your text",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "aliv":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🙄 **Alive**\n\n😒To Find Out If I'm 🤒Dead Or Not\n➥ /alive - dead or not",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "pdft":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📄 **Pdf to Text**\n\n- __a modular Telegram Bot which provides Pdf Tools using PyPdf2 Fork, Send me a pdf file to Move on.__\n\n📚 **Available Commands**\n\n➥ /pdf2txt : __Extract text to Txt file__\n➥ /pinfo : __to Get PDF information__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "audi":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📄➥🗣️ **Pdf to Audiobook**\n\n__A Telegram Bot which converts PDF TO Audio Using Pypdf2 and gTTS__\n__first Send Me a Pdf then im Convert to AudioBook__\n\n📚 **Available Commands**\n\n➥ /audiobook : __Please Reply to PDF file__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "repo":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🗳️ **Report**\n\n__ReportBoT help admins find Those who misbehave in Group.__\n__This command help you to report a message or a user to the admins of the group.__\n\n📚 **Available Commands**\n\n➥ /report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾).",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "nlng":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔗🚫 **Remove URLs in group**\n\n__This module for who sends any kind of link ,remove all links from group.__\n\n➥ List of Links I delete!👇🏼\nhttps\nhttp\nt.me\nwww\ncom",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "must":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔖 **Music tag adder**\n\ni can manage your music channel or group with some cool features like musics tags, getting a short demo of the musics and posting the musics artworks.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "stki":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🖼️➥ɪᴍɢ **Sticker to Image converter**\n\nYou can use this module to **Sticker to Image**,\nfirst send me the Sticker, then i give you a Image.\n\nDon't send me animated sticker or video sticker.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "shar":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="✈️ **Share Text**\n\n📚 **Available Commands**\n\n➥ /share - __get shareable link of any text or link.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "urls":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="⛓️ **𝖴𝗋𝗅 S𝗁𝗈𝗋𝗍𝗇𝖾𝗋**\n__This command help you to short a Url__\n\n📚 **Available Commands**\n\n➥ /short : __𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌__\n⍟ **Example**👇🏼\n/short https://t.me/Music_Galaxy_Dl",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "taga":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="☯️ **TagAll**\n\n__A module for Tagall, i can tag all members in group.__\n\n📚 **Available Commands**\n\n/tagall : just send this command in your group.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "wpsp":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📑 **Web Scrapper**\n\n__This is a web scrapper module, Send me any link for scrapping.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "unzp":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📎 **Unziper**\n\ni can unzip Zip file's.\n\n📚 **Available Commands**\n\nfirst send me zip file.\nthen /unzip to replay  zip file",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "rnmr":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📝 **Renamer module**\n\nHello I'Am a Simple file **Renamer** module.Downbelow my working steps👇🏼\n\n📚 **Available Commands**\n\n•First give me a File\n/rename : Reply To An File With /rename Filename.extension For Renaming.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "gofl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🗂️](https://telegra.ph/file/f8629bb506f9afcd27ff4.jpg) **Go File**\n\n__What is Gofile🤔__\n__Gofile is a free and unlimited file sharing and storage platform.\nYou can use it as a file manager to store all your data, or as a sharing platform to send your files to others. All types of files are supported (files, images, music, videos, pdf etc...). There is no limit, you download at the maximum speed of your connection and most of the service is free.__\n\nWhat is the use of this module ❓👇🏼\nI can upload any media to gofile.io and return the link easily.\n\n📚 **Available Commands**\n\n➥First give me any file img anything\n➥ /go - Replay to any files, then i upload to gofile.io and give you a link of telegram file.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next4")
               ]]
            )
        )

    elif msg.data == "anfl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🗂️ **Anonymous File's Uploader**\n\nI can upload any media to anonfiles.com and return the link easily.\n\n📚 **Available Commands**\n\n/anon - Replay to any files,img eg.. zapGet anonfiles.com link of telegram file.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next4")
               ]]
            )
        )

    elif msg.data == "cv2f":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📽️ 2 📂 **Video to File**\n\n📚 **Available Commands**\n\n➥ /c2f - reply to converting File.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "fltv":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📂 2 📽️ **File to video**\n\nthis module for file to video converte,\n\n📚 **Available Commands**\n\nFist give me a file\n/convert2video - Replay to file for converting to video.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "pasg":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔢 **Password Generater**\n\nThis is a password generator Module, you can generate password from here\n\n📚 **Available Commands**\n\n➥ /genpassword",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next")
               ]]
            )
        )

    elif msg.data == "zomb":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🧟 **Zombies**\n\n__Kick incative members from group. Add me as admin full permission in group.__\n\n📚 **Available Commands**\n\n➥ /inkick - command with required arguments and i will kick members from group.\n➥  /instatus - to check current status of chat member from group.\n➥ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.\n➥ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.\n➥ /dkick - to kick deleted accounts",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "warn":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📛 **Warns**\n\n__Keep your members in check with warnings; stop them getting out of control!__\n__If you're looking for automated warnings, go read about the blocklist module.__\n\n📚 **Available Commands**\n\n➥ /warn <reason>: Warn a user.\n➥ /dwarn <reason>: Warn a user by reply, and delete their message.\n➥ /swarn <reason>: Silently warn a user, and delete your message.\n➥ /warns: See a user's warnings.\n➥ /rmwarn: Remove a user's latest warning.\n➥ /resetwarn: Reset all of a user's warnings to 0.\n➥ /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.\n➥ /warnings: Get the chat's warning settings.\n➥ /setwarnmode <ban/kick/mute>: Set the chat's warn mode.\n➥ /setwarnlimit <number>: Set the number of warnings before users are punished.\n\n- Examples:\n-> /warn @user For disobeying the rules.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "wlcm":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="👋 **Welcome**\n\n__Give your members a warm welcome with the greetings module! Or a sad goodbye... Depends!__\n\n📚 **Available Commands**\n\n➥ /setwelcome reply/text: Set welcome text for group.\n➥ /welcome yes/no/on/off: Enables or Disables welcome setting for group.\n➥ /goodbye <on/off> | noformat : enable/disable | Shows the current goodbye message | settings.\n➥ /resetwelcome: Resets the welcome message to default.\n➥ /setgoodbye reply/text: Sets goodbye text for group.\n➥ /resetgoodbye: Resets the goodbye message to default.\n\n➥ /cleanwelcome yes/no/on/off: Delete the old welcome message, whenever a new member joins.\n➥ /cleangoodbye on/off : Shows or sets the current clean goodbye settings.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "lock":
        await msg.message.edit(
            text="🔐 **Lock**\n\n__Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!__\n\n__The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!__\n\n📚 **Available Commands**\n\n➥ /lock <permission>: Lock Chat permission.\n➥ /unlock <permission>: Unlock Chat permission.\n➥ /locks: View Chat permission.\n➥ /locktypes: Check available lock types!\n\n__Locks can be used to restrict a group's users.__\n__Locking urls will auto-delete all messages with urls, locking stickers will delete all stickers, etc.__\n__Locking bots will stop non-admins from adding bots to the chat.__\n**Example:**\n/lock media: this locks all the media messages in the chat.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "aprl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🔶 **Approval**\n\n__Sometimes, you might trust a user not to send unwanted content.__\n__Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.__\n__Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.__\nThat's what approvals are for - approve of trustworthy users to allow them to send__\n\n📚 **Admin Commands**\n\n**User commands**\n\n➥ /approval: Check a user's approval status in this chat.\n\n**Admin Commands**\n\n➥ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.\n➥ /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.\n➥ /approved: List all approved users.\n\n**Group Owner**\n\n➥ /unapproveall: Unapprove ALL users in a chat. This cannot be undone.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "note":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📖 **Notes**\n\n__Save data for future users with notes!__\n__Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!__\n\n📚 **Admin Commands**\n\n➥ /get <notename>: Get a note.\n\n**Admin commands**\n\n➥ /save <notename> <note text>: Save a new note called word. Replying to a message will save that message. Even works on media!\n➥ /clear <notename>: Delete the associated note.\n➥ /notes: List all notes in the current chat.\n➥ /saved: Same as /notes.\n➥ /clearall: Delete ALL notes in a chat. This cannot be undone.\n➥ /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "rule":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="📜 **Rules**\n\n__Every chat works with different rules; this module will help make those rules clearer!__\n\n📚 **Admin Commands**\n\n**User commands**\n\n➥ /rules: Check the current chat rules.\n\n**Admin commands**\n\n➥ /setrules <text>: Set the rules for this chat.\n➥ /privaterules <yes/no/on/off>: Enable/disable whether the rules should be sent in private.\n➥ /resetrules: Reset the chat rules to default\n➥ /rulesbtn <custom text>: Sets the text of rules button.\n➥ /resetrulesbutton: Reset the text of rules button to default.\n➥ /resetrulesbtn: Same as above.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "admi":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="👮 **Admin**\n\n__Make it easy to promote and demote users with the admin module!__\n\n📚 **Available Commands**\n\n➥ /setgpic :  reply to an image to set as group photo\n➥ /title : [entity] [title]: sets a custom title for an admin. If no [title] provided defaults to Admin\n➥ /setgdes [text] : set group Bio\n➥ /setgtitle : [text] set group title\n➥ /demote : Demote a reply to user message.\n➥ /promote : Promote a reply to user message.\n➥ /fullpromote promote: Promote a member with max rights\n➥ /adminlist: List the admins in the current chat.\n➥ /zombies : Ban deleted accounts\n\n__Sometimes, you promote or demote an admin manually, and Hydrix doesn't realise it immediately. This is because to avoid spamming telegram servers, admin status is cached locally. This means that you sometimes have to wait a few minutes for admin rights to update. If you want to update them immediately, you can use the__ /admincache __command; that'll force Hydrix to check who the admins are again.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "bans":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🚷 **Bans**\n\n__Someone annoying entered your group?__\n__Want to ban/restriction him/her?__\n__This is the plugin for you, easily kick, ban and unban members in a group.__\n\n📚 **Available Commands**\n\n**Admin only:**\n➥ /kick: Kick the user replied or tagged.\n➥ /skick: Kick the user replied or tagged and delete your messsage.\n➥ /dkick: Kick the user replied and delete their message.\n➥ /ban: Bans the user replied to or tagged.\n➥ /sban: Bans the user replied or tagged and delete your messsage.\n➥ /dban: Bans the user replied and delete their message.\n➥ /tban userhandle x(m/h/d): Bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.\n➥ /stban userhandle x(m/h/d): Silently bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.\n➥ /dtban userhandle x(m/h/d): Silently bans a user for x time and delete the replied message. (via reply). m = minutes, h = hours, d = days.\n➥ /unban: Unbans the user replied to or tagged.\n\n**Example**:\n`/ban @username` : this bans a user in the chat.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "fltr":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="💾 **Filters**\n\n__Filters are case insensitive; every time someone says your trigger words, Rose will reply something else! can be used to create your own commands, if desired.__\n\n📚 **Available Commands**\n\n**Admin only:**\n➥ /filters: List all active filters saved in the chat.\n\n**Admin only:**\n➥ /filter ‹keyword› ‹reply message›: Add a filter to this chat. The bot will now reply that message whenever 'keyword'is mentioned. If you reply to a sticker with a keyword, the bot will reply with that sticker.\n\n**Example**:\n`Set a filter:`\n/filter hello Hello there! How are you?\n/filter filtername1|filtername2 Reply Text\n__Using the you can make a single filter work on 2 filternames without manually adding another one.__\n\n/stop ‹filter keyword›: Stop that filter.\n**Note:** __For filters with aliases, if you stop one alias, the filter will stop working on other aliases too.__\n**For Example:** If you stop the filtername1 from above example, the bot will not respond to filtername2\n\n**Chat creator only:**\n\n➥ /removeallfilters: Remove all chat filters at once.\n\n**Note:**\n__Currently there is a limit of 50 filters and 120 aliases per chat.All filter keywords are in lowercase.__",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "unfl":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="🌟 **Unlimited Filter**\n\n__This is an advanced filter module with many capabilities!__\n__Filter is the feature were users can set automated replies for a particular keyword and **HyDrix** will respond whenever a keyword is found the message.__\n__There is no practical limits for my filtering capacity.__\n\n📚 **Available Commands**\n`Filter Commands:`\n➥ /add filter name reply  -  Add filter for name\n➥ /dele filter name  -  Delete filter\n➥ /delall</code>  -  Delete entire filters ⟨Group Owner Only!⟩\n➥ /viewfilters  -  List all filters in chat\n\n**Connection Commands**\n\n➥ /connect groupid  -  Connect your group to my PM. You can also simply use,\n➥ /connections  -  Manage your connections.\n➥ /disconnect - Send this command in your group to disconnect.",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next3")
               ]]
            )
        )

    elif msg.data == "crbn":

        reply1 = await msg.message.reply_text("●○○○")
        await asyncio.sleep(0.5)

        reply2 = await reply1.edit("●●○○")
        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("●●●○")
        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("●●●●")
        await asyncio.sleep(0.5)

        await reply4.delete()

        await msg.message.edit(
            text="[🔳](https://telegra.ph/file/003d78ebbcddfdb489136.jpg) **Carbon Image**\n\n__A Module To Make Carbon Image From TEXT__\n\n📚 **Avaible Command:**\n◉ /carbon : Reply To Any TEXT To Make Carbon Image",
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="next2")
               ]]
            )
        )

    elif msg.data == "delete":
        await msg.message.delete()

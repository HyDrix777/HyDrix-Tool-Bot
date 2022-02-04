import os
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




# id finder

@Client.on_message(filters.private & filters.forwarded)
async def forwarded(_, msg):
    if msg.forward_from:
        text = "Fᴏʀᴡᴀʀᴅ ᴅᴇᴛᴇᴄᴛᴇᴅ! \n\n"
        if msg.forward_from.is_bot:
            text += "**ʙᴏᴛ**"
        else:
            text += "**ᴜsᴇʀ**"
        text += f'\n{msg.forward_from.first_name} \n'
        if msg.forward_from.username:
            text += f'@{msg.forward_from.username} \nɪᴅ : `{msg.forward_from.id}`'
        else:
            text += f'ɪᴅ : `{msg.forward_from.id}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Fᴏʀᴡᴀʀᴅ ᴅᴇᴛᴇᴄᴛᴇᴅ ʙᴜᴛ ᴜɴғᴏʀᴛᴜɴᴀᴛᴇʟʏ, {hidden} ʜᴀs ᴇɴᴀʙʟᴇᴅ ғᴏʀᴡᴀʀᴅɪɴɢ ᴘʀɪᴠᴀᴄʏ, sᴏ I ᴄᴀɴ'ᴛ ɢᴇᴛ ᴛʜᴇɪʀ ɪᴅ",
                quote=True,
            )
        else:
            text = f"Fᴏʀᴡᴀʀᴅ ᴅᴇᴛᴇᴄᴛᴇᴅ. \n\n"
            if msg.forward_from_chat.type == "Channel":
                text += "**Channel**"
            if msg.forward_from_chat.type == "supergroup":
                text += "**Group**"
            text += f'\n{msg.forward_from_chat.title} \n'
            if msg.forward_from_chat.username:
                text += f'@{msg.forward_from_chat.username} \n'
                text += f'ɪᴅ : `{msg.forward_from_chat.id}`'
            else:
                text += f'ɪᴅ : `{msg.forward_from_chat.id}`'
            await msg.reply(text, quote=True)

# group id

@Client.on_message(filters.new_chat_members)
async def welcome(bot, msg):
    bot_id = (await bot.get_me())["id"]
    members = msg.new_chat_members
    for member in members:
        if member.id == bot_id:
            await msg.reply(
                f"Tʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ! \n\nTʜɪs ɢʀᴏᴜᴘ's ɪᴅ ɪs `{msg.chat.id}`"
            )

# private id

@Client.on_message(filters.command("id"))
async def id_(bot: Client, msg: Message):
	if not msg.chat.type == "private":
		main = f"This {msg.chat.type}'s ɪᴅ is `{msg.chat.id}`"
		if msg.reply_to_message:
			if msg.reply_to_message.from_user:
				main = f"{msg.reply_to_message.from_user.first_name}'s ɪᴅ is `{msg.reply_to_message.from_user.id}`"
				if msg.reply_to_message.sticker:
					main += f"\n\nTʜɪs sᴛɪᴄᴋᴇʀ's ɪᴅ ɪs `{msg.reply_to_message.sticker.file_id}`"
		await msg.reply(main)
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Yᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ɪs: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					uname = uname[1:]
				try:
					user = await bot.get_users(uname)
					name = user.mention
					if len(user.first_name) <= 20:
						pass
					elif user.is_bot:
						name = "This Bot"
					else:
						name = "This User"
				except IndexError:
					user = await bot.get_chat(uname)
					name = '@'+user.username if user.username else user.title
				id = user.id
				await msg.reply(f"{name}'s ɪᴅ ɪs `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("Tʜɪs ᴜsᴇʀɴᴀᴍᴇ ɪs ɴᴏᴛ ᴏᴄᴄᴜᴘɪᴇᴅ ʙʏ ᴀɴʏᴏɴᴇ", quote=True)


# Dc finder

@Client.on_message(filters.private & filters.command(["dc"]))
async def dc(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

START_TEXT = "Yᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴄ ɪs : `{}`"
START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('👥 Group', url=f"https://t.me/Music_Galaxy_Dl")
             ]]
        )

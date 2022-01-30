import os
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




# id finder

@Client.on_message(filters.private & filters.forwarded)
async def forwarded(_, msg):
    if msg.forward_from:
        text = "Forward detected! \n\n"
        if msg.forward_from.is_bot:
            text += "**Bot**"
        else:
            text += "**User**"
        text += f'\n{msg.forward_from.first_name} \n'
        if msg.forward_from.username:
            text += f'@{msg.forward_from.username} \nID : `{msg.forward_from.id}`'
        else:
            text += f'ID : `{msg.forward_from.id}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"Forward Detected. \n\n"
            if msg.forward_from_chat.type == "channel":
                text += "**Channel**"
            if msg.forward_from_chat.type == "supergroup":
                text += "**Group**"
            text += f'\n{msg.forward_from_chat.title} \n'
            if msg.forward_from_chat.username:
                text += f'@{msg.forward_from_chat.username} \n'
                text += f'ID : `{msg.forward_from_chat.id}`'
            else:
                text += f'ID : `{msg.forward_from_chat.id}`'
            await msg.reply(text, quote=True)

# group id

@Client.on_message(filters.new_chat_members)
async def welcome(bot, msg):
    bot_id = (await bot.get_me())["id"]
    members = msg.new_chat_members
    for member in members:
        if member.id == bot_id:
            await msg.reply(
                f"Thanks for adding me here! \n\nThis group's ID is `{msg.chat.id}`"
            )

# private id

@Client.on_message(filters.command("id"))
async def id_(bot: Client, msg: Message):
	if not msg.chat.type == "private":
		main = f"This {msg.chat.type}'s ID is `{msg.chat.id}`"
		if msg.reply_to_message:
			if msg.reply_to_message.from_user:
				main = f"{msg.reply_to_message.from_user.first_name}'s ID is `{msg.reply_to_message.from_user.id}`"
				if msg.reply_to_message.sticker:
					main += f"\n\nThis sticker's id is `{msg.reply_to_message.sticker.file_id}`"
		await msg.reply(main)
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Your Telegram ID is: `{msg.from_user.id}`", quote=True)
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
				await msg.reply(f"{name}'s id is `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("This username is not occupied by anyone", quote=True)


BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="SOURCE", url=f"https://github.com/vivek-tp/Info-Bot")
        ]]
    )


@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**🙋🏻‍♂️ First Name :** {update.from_user.first_name}

**🧖‍♂️ Your Second Name :** {last_name}

**🧑🏻‍🎓 Your Username :** {update.from_user.username}

**🆔 Your Telegram ID :** {update.from_user.id}

**🔗 Your Profile Link :** {update.from_user.mention}
""" 
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

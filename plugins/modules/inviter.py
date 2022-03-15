from pyrogram import Client, filters
import pyrogram

class Main:
	des = "Invite a person to chat"
	ver = "1.0"
	cmd_list = {
		"invite + user|id": "invite"
	}

@Client.on_message(filters.me & filters.command("invite",".") & ~filters.private)
def invite_users(app, msg):
	chat_id = msg.chat.id
	reply = msg.reply_to_message
	if reply != None:
		ids = msg.reply_to_message.from_user.id
		try:
		    app.add_chat_members(chat_id, ids)
		except:
			msg.edit("**This person cannot be added**")
	else:
		try: 
			user = msg.text.split(" ", 1)[1]
			try:
				app.add_chat_members(chat_id, user)
			except pyrogram.errors.exceptions.bad_request_400.UserNotMutualContact:
				msg.edit("**This user cannot be added**")
			except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
				msg.edit("**There is no such id**")
			except:
				msg.edit('No contact')
		except:
			msg.edit("**Not enough information**")

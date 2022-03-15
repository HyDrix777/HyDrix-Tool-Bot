from pyrogram import Client, filters
import pyrogram
from pyrogram.types import ChatPermissions
import time


class Main:
	in_help = "promote, demote, ban, unban, kick, mute, unmute"
	cmd_list = {
	"promote" : "raise", 
	"demote" : "downgrade",
	"ban" : "ban", 
	"unban" : "to unravel", 
	"kick" : "to kick",
	"unmute" : "remove mute"
	} 



@Client.on_message(filters.group & filters.command("promote","."))
def promontion(app, msg):
	try:
		user_id = msg.reply_to_message.from_user.id
		try:
			pref = msg.text.split()[1]
		except:
			pref = "Admin"
		app.promote_chat_member(msg.chat.id, user_id)
		app.set_administrator_title(msg.chat.id, user_id, title = pref)
		msg.edit('**Promoted(а)**')
	except pyrogram.errors.exceptions.bad_request_400.ChannelInvalid:
		msg.edit('**This is not a chat**')
	except AttributeError:
		msg.edit('**Who are we promoting?**')


@Client.on_message(filters.group & filters.command("demote","."))
def demontion(app, msg):
  try:
    user_id = msg.reply_to_message.from_user.id
    app.promote_chat_member(msg.chat.id, user_id, False,False,False,False,False,False,False,False)
    msg.edit('**Reduced(а)**')
  except pyrogram.errors.exceptions.bad_request_400.ChannelInvalid:
    msg.edit('**This is not a chat**')
  except AttributeError:
    msg.edit('**Who are we demoting?**')

@Client.on_message(filters.group & filters.command("ban","."))
def baner(app, msg):
	try:
		user_id = msg.reply_to_message.from_user.id
		user_name = msg.reply_to_message.from_user.first_name
		try:
			timer = msg.text.split(" ",1)[1]
			app.kick_chat_member(msg.chat.id, user_id, int(time.time() + int(timer)))
			msg.edit(f"**{user_name} banned on {timer} seconds**")
		except:
			app.kick_chat_member(msg.chat.id, user_id)
			msg.delete()
	except AttributeError:
		msg.edit("**Who to ban?**")
	except pyrogram.errors.exceptions.bad_request_400.ChatAdminRequired:
		msg.edit("**I am not an odmen**")
	except pyrogram.errors.exceptions.bad_request_400.UserAdminInvalid:
		msg.edit("**This sucker is admin**")


@Client.on_message(filters.group & filters.command("unban","."))
def unbaner(app, msg):
  try:
    user_id = msg.reply_to_message.from_user.id
    app.unban_chat_member(msg.chat.id, user_id)
  except AttributeError:
    msg.edit("**Who to ban?**")
  msg.delete()


@Client.on_message(filters.group & filters.command("kick","."))
def kick(app, msg):
	try:
		user_id = msg.reply_to_message.from_user.id
		app.kick_chat_member(msg.chat.id, user_id)
		app.unban_chat_member(msg.chat.id, user_id)
		msg.delete()
	except AttributeError:
		msg.edit("**Who to kick?**")


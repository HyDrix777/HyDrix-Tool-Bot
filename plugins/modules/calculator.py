from pyrogram import filters, Client

class Main:
	des = "Нужно что-то подсчитать?"
	ver = "1.0"
	cmd_list = {
		"calc + репллай или код": "подсчитать"
	}

@Client.on_message(filters.private & filters.command("calc", "."))
def calculator(_, message):
  reply = message.reply_to_message
  if reply is None:
    try:
      example = message.text.split(" ",1)[1]
      message.edit(f"**{eval(example)}**")
    except:
      pass
  else:
    example = message.reply_to_message.text
    message.edit(f"**{eval(example)}**")

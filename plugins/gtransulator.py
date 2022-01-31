from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .list import list


@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            text=f"translated from {translation.src} to {translation.dest}", url="https://cloud.google.com/translate/docs/languages"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"```{translation.text}```", reply_markup=hehek, reply_to_message_id=message.reply_to_message.message_id)
			except:
			   	await message.reply_text(f"```{translation.text}```", reply_markup=hehek, reply_to_message_id=message.reply_to_message.message_id)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 
# Language list

@Client.on_message(filters.command("list"))
async def list(bot: Client, message: Message):
    await message.reply_text(
        text="⍟───List───⍟\n`List is in the form`\n**Language Code** -> **Language**\`naf` -> **Afrikaans**\n⍟──────────⍟",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url="https://t.me/Music_Galaxy_Dl")
           ]]
           )
       )

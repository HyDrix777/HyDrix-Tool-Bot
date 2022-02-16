import os
from pyrogram import Client, filters
from pyrogram.types import *





CALCUL_TEXT = "ᴛʏᴘᴇ ʏᴏᴜʀ ɴᴜᴍʙᴇʀ ᴛᴏ ᴄᴀʟᴄᴜʟᴀᴛᴇ 🔢"
CALCUL_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("DEL", callback_data="DEL"),
        InlineKeyboardButton("AC", callback_data="AC"),
        InlineKeyboardButton("(", callback_data="("),
        InlineKeyboardButton(")", callback_data=")")
        ],[
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("÷", callback_data="/")
        ],[
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("×", callback_data="*")
        ],[
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("-", callback_data="-"),
        ],[
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton("=", callback_data="="),
        InlineKeyboardButton("+", callback_data="+"),
        ]]
    )


@Client.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calc(bot, msg):
    await msg.reply_text(
        text=CALCUL_TEXT,
        reply_markup=CALCUL_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_callback_query()
async def cb_data(bot, msg):
        data = msg.data
        try:
            message_text = msg.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALCUL_TEXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await msg.message.edit_text(
                text=f"{text}\n\n{CALCUL_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCUL_BUTTONS
            )
        except Exception as error:
            print(error)


@Client.on_inline_query()
async def inline(bot, msg):
    if len(msg.data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description=f"New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCUL_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCUL_BUTTONS
                )
            ]
        except Exception as error:
            print(error)
    else:
        try:
            message_text = msg.message.text.split("\n")[0].strip().split("=")[0].strip()
            data = message_text.replace("×", "*").replace("÷", "/")
            text = float(eval(data))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"Results of your input",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {text}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await msg.answer(answers)



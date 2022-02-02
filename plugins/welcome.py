import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.new_chat_members)
async def auto_welcome(bot: Client, msg: Message):
    # from Client import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🤩 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 🤩"
    link_button = "t.me/Tg_Galaxy"
    button_name = os.environ.get("🤩 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 🤩", name_button)
    button_link = os.environ.get("t.me/tg_galaxy", link_button)
    welcome_text = f"Hey {mention}\nWelcome To {group_name}"
    WELCOME_TEXT = os.environ.get("Hi {first} ,\nWelcome to {group_name}♥️\nYour id is {id}", welcome_text)
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          )
       )
    else:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton
                           (
                               button_name, url=button_link
                           )
                   ]  
               ]
           )
       )  

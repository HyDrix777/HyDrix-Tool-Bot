from pyrogram import Client, filters
from gpytranslate import Translator
import sqlite3, string


db = sqlite3.connect("userlanguages.db")
dbc = db.cursor()
dbc.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY,
                                                 chat_lang)""")
db.commit()

default_language = "en"

#Get User IDs and save it in DB
def chat_exists(chat_id, chat_type):
    if chat_type == "private":
        dbc.execute("SELECT user_id FROM users where user_id = ?", (chat_id,))
        return bool(dbc.fetchone())
    raise TypeError("Unknown chat type '%s'." % chat_type)

    
def get_db_lang(chat_id: int, chat_type: str) -> str:
    if chat_type == "private":
        dbc.execute("SELECT chat_lang FROM users WHERE user_id = ?", (chat_id,))
        ul = dbc.fetchone()
    return ul[0] if ul else None
    
def add_chat(chat_id, chat_type):
    if chat_type == "private":
        dbc.execute("INSERT INTO users (user_id) values (?)", (chat_id,))
        db.commit()
        
        
def set_db_lang(chat_id: int, chat_type: str, lang_code: str):
    if chat_type == "private":
        dbc.execute("UPDATE users SET chat_lang = ? WHERE user_id = ?", (lang_code, chat_id))
        db.commit()


@Client.on_message(filters.private, group=-1)
async def check_chat(bot, msg):
    chat_id = msg.chat.id
    chat_type = msg.chat.type

    if not chat_exists(chat_id, chat_type):
        add_chat(chat_id, chat_type)
        set_db_lang(chat_id, chat_type, "en")
        
    
    
##When the user sent /language command, configure the message that the bot should send

@Client.on_message(filters.private & filters.command("language"))
async def language(bot, msg):
    await msg.reply_text(f"**Languages**\n\n__Select the language you want to translate.__\n•/lang (language code)\nExample: ```/lang en``` \n\nList of language codes: https://cloud.google.com/translate/docs/languages   \n\n Send the relevant command. \ud83e\udd20")



@Client.on_message(filters.command("lang") & filters.private)
async def setmylang(bot, msg):
 thelang = msg.command[1]
 await msg.reply(f"{thelang} has been set as your main language👍.")
 set_db_lang(msg.chat.id, msg.chat.type, thelang)



##main translation process

@Client.on_message(filters.private & ~filters.command("tr"))
async def main(bot, msg):
    tr = Translator()
    userlang = get_db_lang(msg.chat.id, msg.chat.type)
    translation = await tr(msg.text, targetlang=[userlang, 'utf-16'])
    language = await tr.detect(msg.text)
    await msg.reply(f"**\ud83c\udf10 Translation**:\n\n```{translation.text}```\n\n**🔍 Detected language:** {language}")
    
@Client.on_message(filters.command("tr") & filters.group)
async def translategroup(bot, msg) -> None:
    tr = Translator()
    if not msg.reply_to_message:
        await msg.reply("Reply to a message to translate")
        return
    if msg.reply_to_message.caption:
        to_translate = msg.reply_to_message.caption
    elif msg.reply_to_message.text:
        to_translate = msg.reply_to_message.text
    try:
        args = msg.text.split()[1].lower()
        if "//" in args:
            language = args.split("//")[0]
            tolanguage = args.split("//")[1]
        else:
            language = await tr.detect(to_translate)
            tolanguage = args
    except IndexError:
        language = await tr.detect(to_translate)
        tolanguage = "en"
    translation = await tr(to_translate,
                              sourcelang=language, targetlang=tolanguage)
    trmsgtext = f"**\ud83c\udf10 Translation**:\n\n```{translation.text}```\n\n**🔍 Detected language:** {language} \n\n **Translated to**: {tolanguage}" 
    await msg.reply(trmsgtext, parse_mode="markdown")

@Client.on_message(filters.command("tr") & filters.private)
async def translateprivatetwo(bot, msg) -> None:
    tr = Translator()
    to_translate = msg.text.split(None, 2)[2]
    language = await tr.detect(msg.text.split(None, 2)[2])
    tolanguage = msg.command[1]
    translation = await tr(to_translate,
                              sourcelang=language, targetlang=tolanguage)
    trmsgtext = f"**\ud83c\udf10 Translation**:\n\n```{translation.text}```\n\n**🔍 Detected language:** {language} \n\n **Translated to**: {tolanguage}" 
    await msg.reply(trmsgtext, parse_mode="markdown")


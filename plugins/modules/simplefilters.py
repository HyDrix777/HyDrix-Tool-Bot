from pyrogram import Client, filters





@Client.on_message(filters.group & filters.regex("hi") | filters.group & filters.regex("Hi"))
async def regex_1(bot, msg):
    await msg.reply_text(f"Hey {msg.from_user.first_name}🤗! How are you.😅")

@Client.on_message(filters.regex("hello") | filters.regex("Hello"))
async def regex_2(bot, msg):
    await msg.reply_text(f"Hello {msg.from_user.first_name} bro👋")

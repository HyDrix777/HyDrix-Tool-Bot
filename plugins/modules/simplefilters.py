from pyrogram import Client, filters





@Client.on_message(filters.private & filters.regex("hi") | filters.private & filters.regex("Hi"))
async def regex_1(bot, msg):
    await msg.reply_text(f"Hi {msg.from_user.first_name} How are you.❤️")


@Client.on_message(filters.private & filters.regex("hello") | filters.private & filters.regex("Hello"))
async def regex_2(bot, msg):
    await msg.reply_text(f"Hello {msg.from_user.first_name} bro, How are you 😌")


@Client.on_message(filters.private & filters.regex("lol") | filters.private & filters.regex("Lol"))
async def regex_3(bot, msg):
    await msg.reply_text(f"Lol 😂 {msg.from_user.first_name} You are soo funny 🤣")

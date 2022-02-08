from pyrogram import filters, Client
from Client import admin_check, extract_user, admin_fliter

@Client.on_message(filters.command(["pin"]) & admin_fliter)
async def pin(_, message: Import.Msg):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()

@Client.on_message(filters.command(["unpin"]) & admin_fliter)
async def unpin(_, message: Import.Msg):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()

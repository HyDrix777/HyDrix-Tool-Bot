from pyrogram import filters, Client




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

from pyrogram import filters, Client
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
from DonLee_Robot_V2.Admins import admin_check, extract_user, admin_fliter

@Client.on_message(filters.command(["pin"], COMMAND_HAND_LER) & admin_fliter)
async def pin(_, message: Import.Msg):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()

@Client.on_message(filters.command(["unpin"], COMMAND_HAND_LER) & admin_fliter)
async def unpin(_, message: Import.Msg):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()

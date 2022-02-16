from pyrogram import Client, filters
from pyrogram.types import Message
import admin_fliter
import COMMAND_HAND_LER


@Client.on_message(
    filters.command(["pin"], COMMAND_HAND_LER) &
    async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)

async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(
    filters.command(["unpin"], COMMAND_HAND_LER) &
    async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)

async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()

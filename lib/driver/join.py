from random import randint

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall

from lib.helpers.decorators import sudo_users
from lib.helpers.filters import public_filters
from lib.tg_stream import app as USER


@Client.on_message(filters.command("join") & public_filters)
@sudo_users
async def join(client, message):
    chat_id = message.chat.id
    try:
        link = await client.export_chat_invite_link(chat_id)
    except BaseException:
        await message.reply("**Error:**\nAdd me as admin of your group!")
        return
    try:
        await USER.join_chat(link)
        await message.reply("**Userbot Joined**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot Already Participant**")


@Client.on_message(filters.command("opengc") & public_filters)
@sudo_users
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    if flags == "channel":
        chat_id = message.chat.title
        type = "channel"
    else:
        chat_id = message.chat.id
        type = "group"
    try:
        await USER.send(
            CreateGroupCall(
                peer=(await USER.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
    except Exception:
        await message.reply(
            "**Error:** Add userbot as admin of your group/channel with permission **Can manage voice chat**"
        )

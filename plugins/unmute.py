from pyrogram import Client, filters
from infog import COMMAND_HAND_LER
from plugins.admin_check import admin_check
from plugins.extract_user import extract_user


@Client.on_message(filters.command(["unban", "unmute"], COMMAND_HAND_LER))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay fine, "
                f"{user_first_name} ക്ക് "
                " can speak again.!"
            )
        else:
            await message.reply_text(
                "Okay, changed ... now "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " You can join the group!"
            )

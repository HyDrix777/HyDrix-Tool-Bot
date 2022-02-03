from pyrogram.errors import ChatAdminRequired, RightForbidden, RPCError
from pyrogram.filters import regex
from pyrogram.types import CallbackQuery, Message




@Client.on_message(command("pin") & admin_filter)
async def pin_message(_, m: Message):
    pin_args = m.text.split(None, 1)
    if m.reply_to_message:
        try:
            disable_notification = True

            if len(pin_args) >= 2 and pin_args[1] in ["alert", "notify", "loud"]:
                disable_notification = False

            await m.reply_to_message.pin(
                disable_notification=disable_notification,
            )
            LOGGER.info(
                f"{m.from_user.id} pinned msgid-{m.reply_to_message.message_id} in {m.chat.id}",
            )

            if m.chat.username:
                # If chat has a username, use this format
                link_chat_id = m.chat.username
                message_link = (
                    f"https://t.me/{link_chat_id}/{m.reply_to_message.message_id}"
                )
            elif (str(m.chat.id)).startswith("-100"):
                # If chat does not have a username, use this
                link_chat_id = (str(m.chat.id)).replace("-100", "")
                message_link = (
                    f"https://t.me/c/{link_chat_id}/{m.reply_to_message.message_id}"
                )
            await m.reply_text(
                tlang(m, "pin.pinned_msg").format(message_link=message_link),
                disable_web_page_preview=True,
            )

        except ChatAdminRequired:
            await m.reply_text(tlang(m, "admin.not_admin"))
        except RightForbidden:
            await m.reply_text(tlang(m, "pin.no_rights_pin"))
        except RPCError as ef:
            await m.reply_text(
                (tlang(m, "general.some_error")).format(
                    SUPPORT_GROUP=SUPPORT_GROUP,
                    ef=ef,
                ),
            )
            LOGGER.error(ef)
    else:
        await m.reply_text("Reply to a message to pin it!")

    return


@Client.on_message(command("unpin") & admin_filter)
async def unpin_message(c: Alita, m: Message):
    try:
        if m.reply_to_message:
            await c.unpin_chat_message(m.chat.id, m.reply_to_message.message_id)
            LOGGER.info(
                f"{m.from_user.id} unpinned msgid: {m.reply_to_message.message_id} in {m.chat.id}",
            )
            await m.reply_text(tlang(m, "pin.unpinned_last_msg"))
        else:
            await c.unpin_chat_message(m.chat.id)
            await m.reply_text(tlang(m, "Unpinned last pinned message!"))
    except ChatAdminRequired:
        await m.reply_text(tlang(m, "admin.not_admin"))
    except RightForbidden:
        await m.reply_text(tlang(m, "pin.no_rights_unpin"))
    except RPCError as ef:
        await m.reply_text(
            (tlang(m, "general.some_error")).format(
                SUPPORT_GROUP=SUPPORT_GROUP,
                ef=ef,
            ),
        )
        LOGGER.error(ef)

    return


@Client.on_message(command("unpinall") & admin_filter)
async def unpinall_message(_, m: Message):
    await m.reply_text(
        "Do you really want to unpin all messages in this chat?",
        reply_markup=ikb([[("Yes", "unpin_all_in_this_chat"), ("No", "close_admin")]]),
    )
    return

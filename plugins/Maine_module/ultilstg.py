import asyncio
from html import escape
from io import BytesIO
from os import remove


from pyrogram import filters
from pyrogram.errors import MessageTooLong, PeerIdInvalid, RPCError
from pyrogram.types import Message
from tswift import Song
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError

from Alita import (
    DEV_USERS,
    LOGGER,
    OWNER_ID,
    PREFIX_HANDLER,
    SUDO_USERS,
    SUPPORT_GROUP,
    SUPPORT_STAFF,
    WHITELIST_USERS,
)
from Alita.bot_class import Alita
from database.antispam_db import GBan
from database.users_db import Users
from Alita.tr_engine import tlang
from Alita.utils.clean_file import remove_markdown_and_html
from Alita.utils.custom_filters import command
from Alita.utils.extract_user import extract_user
from Alita.utils.http_helper import HTTPx, http
from Alita.utils.kbhelpers import ikb
from Alita.utils.parser import mention_html

gban_db = GBan()


@Alita.on_message(command("wiki"))
async def wiki(_, m: Message):
    LOGGER.info(f"{m.from_user.id} used wiki cmd in {m.chat.id}")
    if m.reply_to_message:
        search = m.reply_to_message.text
    else:
        search = m.text.split(None, 1)[1]
    try:
        res = summary(search)
    except DisambiguationError as de:
        await m.reply_text(
            f"Disambiguated pages found! Adjust your query accordingly.\n<i>{de}</i>",
            parse_mode="html",
        )
        return
    except PageError as pe:
        await m.reply_text(f"<code>{pe}</code>", parse_mode="html")
        return
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">Read more...</a>"""
        try:
            await m.reply_text(result, parse_mode="html", disable_web_page_preview=True)
        except MessageTooLong:
            with BytesIO(str.encode(await remove_markdown_and_html(result))) as f:
                f.name = "result.txt"
                await m.reply_document(
                    document=f,
                    quote=True,
                    parse_mode="html",
                )

    return


@Alita.on_message(command("gdpr"))
async def gdpr_remove(_, m: Message):
    if m.from_user.id in SUPPORT_STAFF:
        await m.reply_text(
            "You're in my support staff, I cannot do that unless you are no longer a part of it!",
        )
        return

    Users(m.from_user.id).delete_user()
    await m.reply_text(
        "Your personal data has been deleted.\n"
        "Note that this will not unban you from any chats, as that is telegram data, not Alita data."
        " Flooding, warns, and gbans are also preserved, as of "
        "[this](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/),"
        " which clearly states that the right to erasure does not apply 'for the performance of a task carried out in the public interest', "
        "as is the case for the aforementioned pieces of data.",
        disable_web_page_preview=True,
    )
    await m.stop_propagation()



@Alita.on_message(
    command("gifid") & (filters.group | filters.private),
)
async def get_gifid(_, m: Message):
    if m.reply_to_message and m.reply_to_message.animation:
        LOGGER.info(f"{m.from_user.id} used gifid cmd in {m.chat.id}")
        await m.reply_text(
            f"Gif ID:\n<code>{m.reply_to_message.animation.file_id}</code>",
            parse_mode="html",
        )
    else:
        await m.reply_text(tlang(m, "utils.gif_id.reply_gif"))
    return


@Alita.on_message(
    command("information") & (filters.group | filters.private),
)
async def my_info(c: Alita, m: Message):
    try:
        user_id, name, user_name = await extract_user(c, m)
    except PeerIdInvalid:
        await m.reply_text(tlang(m, "utils.user_info.peer_id_error"))
        return
    except ValueError as ef:
        if "Peer id invalid" in str(ef):
            await m.reply_text(tlang(m, "utils.user_info.id_not_found"))
        return
    try:
        user = Users.get_user_info(int(user_id))
        name = user["name"]
        user_name = user["username"]
        user_id = user["_id"]
    except KeyError:
        LOGGER.warning(f"Calling api to fetch info about user {user_id}")
        user = await c.get_users(user_id)
        name = (
            escape(user["first_name"] + " " + user["last_name"])
            if user["last_name"]
            else user["first_name"]
        )
        user_name = user["username"]
        user_id = user["id"]
    except PeerIdInvalid:
        await m.reply_text(tlang(m, "utils.no_user_db"))
        return
    except (RPCError, Exception) as ef:
        await m.reply_text(
            (tlang(m, "general.some_error")).format(
                SUPPORT_GROUP=SUPPORT_GROUP,
                ef=ef,
            ),
        )
        return

    gbanned, reason_gban = gban_db.get_gban(user_id)
    LOGGER.info(f"{m.from_user.id} used info cmd for {user_id} in {m.chat.id}")

    text = (tlang(m, "utils.user_info.info_text.main")).format(
        user_id=user_id,
        user_name=name,
    )

    if user_name:
        text += (tlang(m, "utils.user_info.info_text.username")).format(
            username=user_name,
        )

    text += (tlang(m, "utils.user_info.info_text.perma_link")).format(
        perma_link=(await mention_html("Click Here", user_id)),
    )

    if gbanned:
        text += f"\nThis user is Globally banned beacuse: {reason_gban}\n"

    if user_id == OWNER_ID:
        text += tlang(m, "utils.user_info.support_user.owner")
    elif user_id in DEV_USERS:
        text += tlang(m, "utils.user_info.support_user.dev")
    elif user_id in SUDO_USERS:
        text += tlang(m, "utils.user_info.support_user.sudo")
    elif user_id in WHITELIST_USERS:
        text += tlang(m, "utils.user_info.support_user.whitelist")

    await m.reply_text(text, parse_mode="html", disable_web_page_preview=True)

    return


@Alita.on_message(command("weebify"))
async def weebify(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Please reply to a message or enter text after command to weebify it.",
        )
        return
    if not args:
        await m.reply_text(tlang(m, "utils.weebify.weebify_what"))
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "卂 乃 匚 刀 乇 下 厶 卄 工 丁 长 乚 从 𠘨 口 尸 㔿 尺 丂 丅 凵 リ 山 乂 丫 乙".split()

    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        (tlang(m, "utils.weebify.weebified_string").format(string=string)),
    )
    LOGGER.info(f"{m.from_user.id} weebified '{args}' in {m.chat.id}")

    return

@Alita.on_message(
    command("info") & (filters.group | filters.private),
)
async def my_info(c: Alita, m: Message):
    try:
        user_id, name, user_name = await extract_user(c, m)
    except PeerIdInvalid:
        await m.reply_text(tlang(m, "utils.user_info.peer_id_error"))
        return
    except ValueError as ef:
        if "Peer id invalid" in str(ef):
            await m.reply_text(tlang(m, "utils.user_info.id_not_found"))
        return
    try:
        user = Users.get_user_info(int(user_id))
        name = user["name"]
        user_name = user["username"]
        user_id = user["_id"]
    except KeyError:
        LOGGER.warning(f"Calling api to fetch info about user {user_id}")
        user = await c.get_users(user_id)
        name = (
            escape(user["first_name"] + " " + user["last_name"])
            if user["last_name"]
            else user["first_name"]
        )
        user_name = user["username"]
        user_id = user["id"]
    except PeerIdInvalid:
        await m.reply_text(tlang(m, "utils.no_user_db"))
        return
    except (RPCError, Exception) as ef:
        await m.reply_text(
            (tlang(m, "general.some_error")).format(
                SUPPORT_GROUP=SUPPORT_GROUP,
                ef=ef,
            ),
        )
        return

    gbanned, reason_gban = gban_db.get_gban(user_id)
    LOGGER.info(f"{m.from_user.id} used info cmd for {user_id} in {m.chat.id}")

    text = (tlang(m, "utils.user_info.info_text.main")).format(
        user_id=user_id,
        user_name=name,
    )

    if user_name:
        text += (tlang(m, "utils.user_info.info_text.username")).format(
            username=user_name,
        )

    text += (tlang(m, "utils.user_info.info_text.perma_link")).format(
        perma_link=(await mention_html("Click Here", user_id)),
    )

    if gbanned:
        text += f"\nThis user is Globally banned beacuse: {reason_gban}\n"

    if user_id == OWNER_ID:
        text += tlang(m, "utils.user_info.support_user.owner")
    elif user_id in DEV_USERS:
        text += tlang(m, "utils.user_info.support_user.dev")
    elif user_id in SUDO_USERS:
        text += tlang(m, "utils.user_info.support_user.sudo")
    elif user_id in WHITELIST_USERS:
        text += tlang(m, "utils.user_info.support_user.whitelist")

    await m.reply_text(text, parse_mode="html", disable_web_page_preview=True)

    return

@Alita.on_message(command("past"))
async def paste_it(_, m: Message):
    await m.reply_text("Nekobin is currently not reachable! :) will fix it soon !")
    return
    """
    replymsg = await m.reply_text((tlang(m, "utils.paste.pasting")), quote=True)
    try:
        if m.reply_to_message:
            if m.reply_to_message.document:
                dl_loc = await m.reply_to_message.download()
                with open(dl_loc) as f:
                    txt = f.read()
                remove(dl_loc)
            else:
                txt = m.reply_to_message.text
        else:
            txt = m.text.split(None, 1)[1]

        url = (await paste(txt))[0]
        await replymsg.edit_text(
            (tlang(m, "utils.paste.pasted_nekobin")),
            reply_markup=ikb([[((tlang(m, "utils.paste.nekobin_btn")), url, "url")]]),
        )
        LOGGER.info(f"{m.from_user.id} used paste cmd in {m.chat.id}")
    except Exception as e:
        await replymsg.edit_text(f"Error: {e}")
        return

    return
    """




__PLUGIN__ = "utils"
__alt_name__ = ["util", "misc", "tools"]

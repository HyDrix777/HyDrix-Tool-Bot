from asyncio import (gather, get_event_loop, sleep)
from pyrogram import (Client, filters, idle)



print("[INFO]: Checking... Your Details")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: Code running by Hydrix")
arq = None


async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Luna", "Hydrix")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Hydrix")
    else:
        responsess = responsee
    if "Who is Nazriya?" in responsess:
        responsess2 = responsess.replace("Who is Hydrix?", "King of TG")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@Client.on_message(
    ~filters.private | ~filters.group
    & filters.text
    & ~filters.command("start")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@Client.on_message(
    filters.private | ~filters.group
    & ~filters.command("start")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        await message.reply_text("Ufff... Ignoring ....👻")
        return
    await type_and_send(message)


@Client.on_message(filters.command("hi") & ~filters.edited)
async def startt(_, message):
    await message.reply_text("Hai🧞, its me hydrix")


async def main():
    global arq
    session = ClientSession()

    await bot.start()
    print(
        """
Nazriya Is Deployed Successfully.
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())

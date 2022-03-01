from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from pyrogram.types import Message

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

    
BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "News Channel", url="https://t.me/szteambots"
                    )
                ],
            ]
          )

@Client.on_message(filters.command(["carbon"]))

async def carbon_func(client, message):
    TEXT = f"""
Carbon Genarated Successfully✅

࿂ **Generated By** : [szrosebot](https://t.me/szrosebot)
࿂ **Requestor** :. {message.from_user.mention}
࿂ **Powered By **  : [szteambots](https://t.me/szteambots)
"""
    if not message.reply_to_message:
        text = get_text(message)
        carbon = await make_carbon(text)
        return await client.send_photo(message.chat.id, carbon,caption=TEXT,reply_markup= BUTTON)
    m = await message.reply_text("`Preparing`")   
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await client.send_photo(message.chat.id, carbon,caption=TEXT,reply_markup= BUTTON)
    await m.delete()
    carbon.close()

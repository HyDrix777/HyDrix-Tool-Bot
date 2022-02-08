from os import environ
import aiohttp
from pyrogram import Client, filters


    


@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'❗ Here is your [`{short_link}`]({short_link}) \n\n 〽️ Powered by @GroupDcBots', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://shortzon.com/api'
    params = {'api':'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

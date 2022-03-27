import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('ᴍʏ ɢʀᴏᴜᴘ', url='https://t.me/Music_Galaxy_Dl')]])


@Client.on_message(filters.command("covid"))
async def reply_info(bot, update):
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(query),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--

🌎 **Globle Covid 19 Stats** 🌎
🗺️ Country : `{country}`
🔖 Actived : `{active}`
📊 Confirmed : `{confirmed}`
☠️ Deaths : `{deaths}`
📟 ID : `{info_id}`
😷 Last Update : `{last_update}`
🔽 Latitude : `{latitude}`
🔼 Longitude : `{longitude}`
🧑‍⚕️ Recovered : `{recovered}`

⚡Powered by: @HTGToolBot"""
        return covid_info
    except Exception as error:
        return error

import os
import io
import re
import requests
import mutagen
from mutagen.mp3 import MP3
from music_tag import load_file
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from configs import Config



    
@Client.on_message(filters.group & filters.audio | filters.channel & filters.audio)
async def music(bot, m):
    fname = m.audio.file_name
    file = await m.download("temp/file.mp3")
    music = load_file("temp/file.mp3")
    t = f"{music['title']}"
    a = f"{music['artist']}"
    al = f"{music['album']}"
    g = f"{music['genre']}"
    c = f"{music['comment']}"
    l = f"{music['lyrics']}"
    try:
        artwork = music['artwork']
        image_data = artwork.value.data
        img = Image.open(io.BytesIO(image_data))
        img.save("artwork.jpg")
    except ValueError:
        artwork = None

    if fname.__contains__("@") or fname.__contains__(".me/"):
        fname = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', fname).replace('  ', ' ')
    if fname.startswith(' '):
        fname = fname.split(' ', 1)[+1]

    if a.__contains__("@") or a.__contains__(".me/"):
        a = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', a).replace('  ', ' ')
    if a.startswith(' '):
        a = a.split(' ', 1)[+1]

    if g.__contains__("@") or g.__contains__(".me/"):
        g = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', g).replace('  ', ' ')
    if g.startswith(' '):
        g = g.split(' ', 1)[+1]

    if al.__contains__("@") or al.__contains__(".me/"):
        al = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', al).replace('  ', ' ')
    if al.startswith(' '):
        al = al.split(' ', 1)[+1]

    if t.__contains__("@") or t.__contains__(".me/"):
        t = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', t).replace('  ', ' ')
    if t.startswith(' '):
        t = t.split(' ', 1)[+1]

    if l.__contains__("@") or l.__contains__(".me/"):
        l = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', l).replace('  ', ' ')
    if l.startswith(' '):
        l = l.split(' ', 1)[+1]

    if c.__contains__("@") or c.__contains__(".me/"):
        c = re.sub(r'\S*[t|T].me\S*|\S*@\S*', '', c).replace('  ', ' ')
    if c.startswith(' '):
        c = c.split(' ', 1)[+1]

    if artwork is not None:
        try:
            await bot.send_photo(
                chat_id=m.chat.id,
                caption="✏️**Title:**" + a + " - " + t + "🎼" + "\n" + "👤 **Artist:** " + a + "\n" + "💽 **Album:** " + al + "\n" + "🎼 **Genre:** " + g + "\n\n" + f"🔰 : @HTGToolBot",
                photo=open('artwork.jpg', 'rb')
            )
        except Exception as e:
            print(e)

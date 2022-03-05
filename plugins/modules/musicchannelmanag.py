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
from config import Config



    
@Client.on_message(filters.group & filters.audio)
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
                caption="🎤" + a + " - " + t + "🎼" + "\n\n" + f"🆔👉 {Config.USERNAME}",
                photo=open('artwork.jpg', 'rb')
            )
        except Exception as e:
            print(e)

    audio = MP3(file)
    length = audio.info.length * 0.33
    l2 = (audio.info.length * 0.33) + 60
    if audio.info.length > l2:
        os.system("ffmpeg -ss " + str(length) + " -t 60 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
    else:
        os.system("ffmpeg -ss 0 -t 60 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
    sendVoice(m.chat.id, "temp/output.ogg", f"🎤{a} - {t}🎼\n\n🆔👉 {Config.USERNAME}")
        
    music.remove_tag('comment')
    music.remove_tag('artist')
    music.remove_tag('lyrics')
    music.remove_tag('title')
    music.remove_tag('album')
    music.remove_tag('genre')
    music['artist'] = a + Config.custom_tag
    music['title'] = t + Config.custom_tag
    music['album'] = al + Config.custom_tag
    music['genre'] = g + Config.custom_tag
    music['comment'] = c + Config.custom_tag
    music['lyrics'] = l + Config.custom_tag
    music.save()

    if Config.CAPTION == "TRUE":
        caption = "✏️ Title: " + t + "\n" + "👤 Artist: " + a + "\n" + "💽 Album: " + al + "\n" + "🎼 Genre: " + g + "\n\n" + f"🆔👉 {Config.USERNAME}"
    else:
        caption = m.caption if m.caption else " "

    try:
        if artwork is not None:
            await bot.send_audio(
                chat_id=m.chat.id,
                file_name=fname,
                performer=a,
                title=t,
                duration=m.audio.duration,
                caption=caption,
                thumb=open('artwork.jpg', 'rb'),
                audio='temp/file.mp3'
            )
        elif artwork is None:
            await bot.send_audio(
                chat_id=m.chat.id,
                file_name=fname,
                performer=a,
                title=t,
                duration=m.audio.duration,
                caption=caption,
                audio='temp/file.mp3'
            )
    except Exception as e:
        print(e)

def sendVoice(chat_id,file_name,text):
    url = "https://api.telegram.org/bot%s/sendVoice"%(Config.BOT_TOKEN)
    files = {'voice': open(file_name, 'rb')}
    data = {'chat_id' : chat_id, 'caption' : text}
    r= requests.post(url, files=files, data=data)

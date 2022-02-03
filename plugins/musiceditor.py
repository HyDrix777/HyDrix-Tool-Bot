import os
import io
from PIL import Image
from pyromod import listen
from music_tag import load_file




   
@bot.on_message(filters.private & filters.audio)
async def tag(bot, m):
    mes = await m.reply("`Downloading...`", parse_mode='md')
    await m.download("temp/music.mp3")
    music = load_file("temp/music.mp3")

    try:
        artwork = music['artwork']
        image_data = artwork.value.data
    except ValueError:
        image_data = None

    await mes.delete()
    fname = await bot.ask(m.chat.id,'`Send the Filename`', filters=filters.text, parse_mode='Markdown')
    title = await bot.ask(m.chat.id,'`Send the Title name`', filters=filters.text, parse_mode='Markdown')
    artist = await bot.ask(m.chat.id,'`Send the Artist(s) name`', filters=filters.text, parse_mode='Markdown')
    answer = await bot.ask(m.chat.id,'`Send the Artwork or` /skip', filters=filters.photo | filters.text, parse_mode='Markdown')
    music.remove_tag('artist')
    music.remove_tag('title')
    music.remove_tag('artwork')
    music['artist'] = artist.text
    music['title'] = title.text

    if answer.text and ("/skip" in answer.text):
        if image_data is not None:
            img = Image.open(io.BytesIO(image_data))
            img.save("temp/artwork.jpg")
        music.save()
        try:
            await bot.send_audio(
                chat_id=m.chat.id,
                file_name=fname.text,
                performer=artist.text,
                title=title.text,
                duration=m.audio.duration,
                audio='temp/music.mp3'
            )
        except Exception as e:
            print(e)

    elif answer.photo:
        await bot.download_media(message=answer.photo, file_name="temp/artwork.jpg")
        with open('temp/artwork.jpg', 'rb') as img_in:
            music['artwork'] = img_in.read()
        music.save()
        try:
            await bot.send_audio(
                chat_id=m.chat.id,
                file_name=fname.text,
                performer=artist.text,
                title=title.text,
                duration=m.audio.duration,
                thumb=open('temp/artwork.jpg', 'rb'),
                audio='temp/music.mp3'
            )
        except Exception as e:
            print(e)

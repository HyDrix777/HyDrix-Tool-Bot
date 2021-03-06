import os
from utils import extract_user, get_file_id, get_poster, last_online
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import time
from datetime import datetime



@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Searching ImDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("No results Found")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('Here is what i found on IMDb', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Give me a movie Name')

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')} - {imdb.get('year')}",
                    url=imdb['url'],
                )
            ]
        ]
    if imdb.get('poster'):
        await query.message.reply_photo(photo=imdb['poster'], caption=f"IMDb Data:\n\nš· Title:<a href={imdb['url']}>{imdb.get('title')}</a>\nš­ Genres: {imdb.get('genres')}\nš Year:<a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\nš Rating: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\nš StoryLine: <code>{imdb.get('plot')} </code>", reply_markup=InlineKeyboardMarkup(btn))
        await query.message.delete()
    else:
        await query.message.edit(f"IMDb Data:\n\nš· Title:<a href={imdb['url']}>{imdb.get('title')}</a>\nš­ Genres: {imdb.get('genres')}\nš Year:<a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\nš Rating: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\nš StoryLine: <code>{imdb.get('plot')} </code>", reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await query.answer()

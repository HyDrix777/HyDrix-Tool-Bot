from pyrogram import Client, filters
from pyrogram.types import *
import time
import requests
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urlparse






def gp(url):
    scraper = cloudscraper.create_scraper(allow_brotli=False)
    src = scraper.get(url)
    header = { "referer": src.url }
    src = scraper.get(url, headers=header)
    
    bs4 = BeautifulSoup(src.content, 'lxml')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    time.sleep(10) 
    
    k = urlparse(url)
    URL = f'{k.scheme}://{k.netloc}/links/go'
    src = scraper.post(URL, data=data, headers=header).json()

    return src


@Client.on_message(
    filters.command("gp", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def gplink(_, message): 

    link = message.command[1]

    gpLink = gp(url=link)
    
    await message.reply_text(f"{gpLink}")

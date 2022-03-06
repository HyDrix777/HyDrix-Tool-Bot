from asyncio import gather
import aiofiles
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pyrogram.types import Message
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
from io import BytesIO



async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

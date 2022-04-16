from pyrogram import Client
from pytgcalls import PyTgCalls

from lib.config import API_HASH, API_ID, SESSION_NAME

app = Client(SESSION_NAME, API_ID, API_HASH)
call_py = PyTgCalls(app)

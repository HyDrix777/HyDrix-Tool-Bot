import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
import os


from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}


LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

---------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '784589736').split()]
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", True))
IMDB = bool((environ.get('IMDB', True)))
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
BOT_USERNAME = environ.get("BOT_USERNAME", "HTGToolBot")
COMMAND_PREFIXES = (environ.get("COMMAND_PREFIXES", "/ ! .").split())

----------
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
OWNER_NAME = getenv("OWNER_NAME", "Hydrix")
ALIVE_NAME = getenv("ALIVE_NAME", "Hydrix")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Androgobs")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "songdownload_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tg_galaxy")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736 5013387325").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/61bed9716df9e4f1be322.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Hydrayt777/HyDrix-Tool-Bot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e89f7dcacc1d4f18e7e99.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/263702418d8bd747fffa1.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a880bb55eb457f70afebc.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/1006d09ee8e606242532d.jpg")

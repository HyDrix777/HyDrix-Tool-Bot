import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
import os


PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001784386455')).split()]
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))


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



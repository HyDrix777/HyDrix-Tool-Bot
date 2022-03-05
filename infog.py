import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
import os




AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w")

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '784589736').split()]
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", True))
IMDB = bool((environ.get('IMDB', True)))
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

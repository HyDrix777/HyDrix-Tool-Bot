import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
import os
import logging




DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Tg_galaxy")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())

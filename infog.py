import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
import os


ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '784589736').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100

START_TXT = """Hey {}, Iam a Guess Game Bot 

Hope You Enjoyed The Bot
"""

GUESS_COUNT = int(environ.get("GUESS_COUNT", ""))

MAX_GUESSES = int(environ.get("MAX_GUESSES", ""))

SECRET_WORD = environ.get("Any word that you want your users to guess")

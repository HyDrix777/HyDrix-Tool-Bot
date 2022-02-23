import re
from os import environ
id_pattern = re.compile(r'^.\d+$')



ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '784589736').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100
MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))
SESSION_NAME = os.environ.get("Torrent-Search-Bot")

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

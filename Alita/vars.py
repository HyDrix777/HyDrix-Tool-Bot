from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    APP_ID = int(config("APP_ID", default=None))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=784589736))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-1001784386455))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="784589736").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    DB_URI = config("DB_URI", default="mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="Cluster0")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="songdownload_group")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="Tg_galaxy")
    ENABLED_LOCALES = [str(i) for i in config("ENABLED_LOCALES", default="en").split()]
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = "@HTGToolBot"
    BOT_ID = "5219376297"
    BOT_NAME = "Hydrix Tool Bot"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w"
    APP_ID = "18891187"  # Your APP_ID from Telegram
    API_HASH = "7d120384f48b2a86fa2b9e9772a28af6"  # Your APP_HASH from Telegram
    OWNER_ID = "784589736"  # Your telegram user id
    MESSAGE_DUMP = "-1001784386455"  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = ["784589736"]
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME = "Cluster0"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "songdownload_group"
    SUPPORT_CHANNEL = "Tg_galaxy"
    ENABLED_LOCALES = ["ENABLED_LOCALES"]
    VERSION = "VERSION"
    WORKERS = 8

import os
import logging


LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)




class Config(object):
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@HTGToolBot")


bot = Config.BOT_USERNAME
class CMD(object):
    RENAME = ["rename", f"rename@{bot}"]

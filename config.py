import os

class Config(object):
    CONVERT_API = os.environ.get("GN4pzf2BHGr7nzHE")
    MAX_FILE_SIZE = os.environ.get("8")
    OWNER_ID = os.environ.get("OWNER_ID")
    PDF_THUMBNAIL = "./thumbnail.jpeg"
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "

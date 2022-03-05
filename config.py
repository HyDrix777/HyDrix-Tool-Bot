import os

class Config(object):
    USERNAME = os.environ.get("@HTGToolBot")
    CAPTION = os.environ.get("false")
    CUSTOM_TAG = os.environ.get("false")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "

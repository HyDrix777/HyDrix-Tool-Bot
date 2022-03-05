import os

class Config(object):
    USERNAME = os.environ.get('CHANNEL_USERNAME')
    CAPTION = os.environ.get("DYNAMIC_CAPTION")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "

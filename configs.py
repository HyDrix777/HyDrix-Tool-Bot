import os







class Config(object):

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "
    


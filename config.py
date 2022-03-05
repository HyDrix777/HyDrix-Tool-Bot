import os

class Config(object):
    AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BOT_TOKEN = os.environ.get('bot_token', "5219376297:AAFydXWjPg47TlZ4QnVkc2egji4mPMq0_2w")
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "

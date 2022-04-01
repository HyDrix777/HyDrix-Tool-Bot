import os







class Config(object):
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
    INPUT_REQUIRED = """❗ **Arguments Required**"""
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
    ADMIN_REQUIRED = """❗<b>I do not know where to start Bii..Add Me Again with all admin rights.</b>"""
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
    FETCHING_INFO = """<b>Finding Group datas...</b>"""
    STATUS = """{}\n<b>ChatMember Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>"""

    DEF_WATER_MARK_FILE = "Uploaded by: @HTgToobot"
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DATABASE_URL = os.environ.get("mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "
    


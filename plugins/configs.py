import os


class Config(object):
    SESSION_NAME = os.environ.get("Torrant ")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))

import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6803879488:AAFZAryvguDSx9DCXUXfeHSIbwL2b9HjOu0")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "10471716"))
    API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")

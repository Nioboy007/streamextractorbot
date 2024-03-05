import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6365859811:AAF1Aj_VrbdxS9aPED2PqjwRaeEi4fcm_JE")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "10471716"))
    API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6883997969").split())

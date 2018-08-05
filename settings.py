import json


def init():
    global GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, SECRET_CHATS
    GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, SECRET_CHATS = range(10)
    with open('es_strings.json', encoding='UTF-8') as f:
        global strings
        strings = json.load(f)

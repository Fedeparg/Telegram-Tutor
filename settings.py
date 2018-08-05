import json


def init():
    global MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS
    MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS = range(9)
    with open('es_strings.json', encoding='UTF-8') as f:
        global strings
        strings = json.load(f)

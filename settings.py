import json


def init():
    global MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, \
        SECRET_CHATS
    MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, SECRET_CHATS = \
        range(11)
    with open('es_strings.json', encoding='UTF-8') as f:
        global strings
        strings = json.load(f)

import json
import logging

def init():
    logging.basicConfig(filename="log.txt",
                        level=logging.INFO,
                        format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    global GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, SECRET_CHATS
    GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, CHAT_PREVIEW, VIDEO_NOTES, SECRET_CHATS = range(
        10)
    with open('str/es_strings.json', encoding='UTF-8') as f:
        global strings
        strings = json.load(f)

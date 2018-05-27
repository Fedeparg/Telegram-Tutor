#!/usr/bin/env python

import english_strings as en_str
import spanish_strings as es_str
import logging
from telegram import *
from telegram.ext import *
import time
import re

"""Start logging"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
"""Sates of the automaton"""
LANGUAGE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS = range(8)
"""Pattern for language selection"""
pattern = re.compile("English*")

def help(bot, update):
    update.message.reply_text(en_str.help)

def ayuda(bot, update):
    update.message.reply_text(es_str.help)


def start(bot, update):
    """Method used to start the automaton"""
    reply_keyboard = [['Español 🇪🇸', 'English 🇬🇧']]
    update.message.reply_markdown('🇬🇧 🇪🇸 ?',
    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return LANGUAGE


def language_selected(bot, update):
    """Select language based on first selection. Can be changed if the user uses the command of the other language"""
    mssg = update.message
    if pattern.match(mssg.text):
        update.message.reply_markdown(en_str.language1 + 
            mssgfrom_user.first_name + '.', reply_markup = ReplyKeyboardRemove())
        update.message.reply_markdown(en_str.language2)
        update.message.reply_markdown(en_str.language3)
        return MESSAGES
    else:
        update.message.reply_markdown(es_str.language1 + 
            mssg.from_user.first_name + '.', reply_markup = ReplyKeyboardRemove())
        update.message.reply_markdown(es_str.language2)
        update.message.reply_markdown(es_str.language3)
        update.message.reply_markdown(es_str.nextsection)
        return MESSAGES


def messages_es(bot, update):
    """Send information about messages"""
    update.message.reply_markdown(es_str.messages1)
    update.message.reply_markdown(es_str.messages2)
    update.message.reply_markdown(es_str.messages3)
    update.message.reply_markdown(es_str.nextsection)
    return GROUPS

def groups_es(bot, update):
    """Send information about groups"""
    update.message.reply_markdown(es_str.groups1)
    update.message.reply_markdown(es_str.groups2)
    update.message.reply_markdown(es_str.groups3)
    update.message.reply_markdown(es_str.nextsection)
    return CHANNELS

def channels_es(bot, update):
    """Send information about channels"""
    update.message.reply_markdown(es_str.channels1)
    update.message.reply_markdown(es_str.nextsection)
    return CLOUD

def cloud_es(bot, update):
    """Send information about cloud storage"""
    update.message.reply_markdown(es_str.cloud1)
    update.message.reply_markdown(es_str.cloud2)
    update.message.reply_markdown(es_str.nextsection)
    return BOTS

def bots_es(bot, update):
    """Send information about Bbts"""
    update.message.reply_markdown(es_str.bots1)
    update.message.reply_markdown(es_str.bots2)
    update.message.reply_markdown(es_str.bots3)
    return MEDIA

def media_es(bot, update):
    """Checks if sent message was a gif from @gif bot"""
    if update.message.document.file_name == 'giphy.mp4':
        update.message.reply_markdown(es_str.media1)
        update.message.reply_markdown(es_str.media2)
        update.message.reply_markdown(es_str.media3)
        return SECRET_CHATS
    else:
        update.message.reply_markdown(es_str.media_error)
    
def secret_chats(bot, update):
    """Send information about secret chats"""
    update.message.reply_markdown(es_str.secret_chats1)
    update.message.reply_markdown(es_str.secret_chats2)
    update.message.reply_markdown(es_str.secret_chats3)
    update.message.reply_markdown(es_str.FIN)
    return ConversationHandler.END

def test(bot, update):
    """Method for develop pruposes. Not used by users"""
    print(update)


def cancel(bot, update):
    """Ends the automaton"""
    return ConversationHandler.END

def error(bot, update):
    """Notify the user that his message wasn't expected by the automaton."""
    update.message.reply_markdown('Error. Not expected message')

def main():
    # Telegram Bot Authorization Token
    updater = Updater('BOTTOKEN')
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        allow_reentry = True,

        states={
            LANGUAGE: [MessageHandler(Filters.text, language_selected)],

            MESSAGES: [CommandHandler('siguiente', messages_es)],

            GROUPS: [CommandHandler('siguiente', groups_es)],

            CHANNELS: [CommandHandler('siguiente', channels_es)],

            CLOUD:[CommandHandler('siguiente', cloud_es)],

            BOTS: [CommandHandler('siguiente', bots_es)],

            MEDIA: [MessageHandler(Filters.document, media_es)],

            SECRET_CHATS: [MessageHandler(Filters.sticker, secret_chats)]
        },
        fallbacks=[CommandHandler('cancel', cancel),
        MessageHandler(Filters.sticker, error)]
    )

    updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
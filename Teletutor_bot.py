#!/usr/bin/env python

from functions_es import *
from guide_spa import *
import logging
from telegram.ext import *

"""Start logging"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
"""Sates of the automaton"""
MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS = range(9)
"""Pattern for introduction selection"""


def start(bot, update):
    return language_es(bot, update)


def test(bot, update):
    """Method for develop pruposes. Not used by users"""
    print(update)


def error(bot, update):
    """Notify the user that his message wasn't expected by the automaton."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    update.message.reply_markdown(es_str.error)


def main():
    # Telegram Bot Authorization Token
    updater = Updater('BOTTOKEN')
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document, test))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        allow_reentry=True,

        states={
            MODE_SELECTION: [CommandHandler('guia', guide_es),
                             CommandHandler('tutorial', tutorial_es)],

            GUIDE: [CallbackQueryHandler(button_guide)],

            MESSAGES: [CommandHandler('siguiente', messages_es)],

            GROUPS: [CommandHandler('siguiente', groups_es)],

            CHANNELS: [CommandHandler('siguiente', channels_es)],

            CLOUD: [CommandHandler('siguiente', cloud_es)],

            BOTS: [CommandHandler('siguiente', bots_es)],

            MEDIA: [MessageHandler(Filters.document, media_es)],

            SECRET_CHATS: [MessageHandler(Filters.sticker, secret_chats_es)]
        },
        fallbacks=[CommandHandler('stop', stop_es),
                   MessageHandler(Filters.all, error)]
    )

    updater.dispatcher.add_handler(conv_handler)

    # log all errors
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import logging

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler

from functions_es import *
import guide_spa as g_spa
import settings as st

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

"""Starts the automaton"""
st.init()


def start(bot, update):
    return start_es(bot, update)


def test(bot, update):
    """Method for develop pruposes. Not used by users"""
    print(update)


def main():
    # Telegram Bot Authorization Token
    updater = Updater('BOTTOKEN')
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document, test))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('guia', g_spa.guide_es), CommandHandler(
            'tutorial', tutorial_es)],
        allow_reentry=True,

        states={

            st.GUIDE: [CallbackQueryHandler(g_spa.button_guide),
                       CommandHandler('tutorial', tutorial_es)],

            st.MESSAGES: [CommandHandler('siguiente', messages_es)],

            st.GROUPS: [CommandHandler('siguiente', groups_es)],

            st.CHANNELS: [CommandHandler('siguiente', channels_es)],

            st.CLOUD: [CommandHandler('siguiente', cloud_es)],

            st.BOTS: [CommandHandler('siguiente', bots_es)],

            st.MEDIA: [MessageHandler(Filters.document, media_es)],

            st.CHAT_PREVIEW: [MessageHandler(Filters.sticker, chat_preview_es)],

            st.VIDEO_NOTES: [CommandHandler('siguiente', video_notes_es)],

            st.SECRET_CHATS: [MessageHandler(
                Filters.video_note, secret_chats_es)]
        },
        fallbacks=[CommandHandler('stop', stop_es),
                   MessageHandler(Filters.all, error)]
    )

    updater.dispatcher.add_handler(CommandHandler('start', start_es))
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

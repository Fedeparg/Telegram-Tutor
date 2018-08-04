#!/usr/bin/env python
from telegram.ext import *
from functions_es import *
from guide_spa import *
import settings as st

"""Start logging"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

"""Starts the automaton"""
st.init()


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
            st.MODE_SELECTION: [CommandHandler('guia', guide_es),
                                CommandHandler('tutorial', tutorial_es)],

            st.GUIDE: [CallbackQueryHandler(button_guide)],

            st.MESSAGES: [CommandHandler('siguiente', messages_es)],

            st.GROUPS: [CommandHandler('siguiente', groups_es)],

            st.CHANNELS: [CommandHandler('siguiente', channels_es)],

            st.CLOUD: [CommandHandler('siguiente', cloud_es)],

            st.BOTS: [CommandHandler('siguiente', bots_es)],

            st.MEDIA: [MessageHandler(Filters.document, media_es)],

            st.SECRET_CHATS: [MessageHandler(Filters.sticker, secret_chats_es)]
        },
        fallbacks=[CommandHandler('stop', stop_es),
                   MessageHandler(Filters.all, error)]
    )

    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
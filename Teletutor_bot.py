#!/usr/bin/env python

import strings_en as en_str
from functions_es import *
from guide_spa import *
import logging
from telegram import *
from telegram.ext import *
import re

"""Start logging"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
"""Sates of the automaton"""
LANGUAGE, MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS = range(10)
"""Pattern for introduction selection"""
pattern = re.compile("English*")


def help(bot, update):
    update.message.reply_text(en_str.help)


def start(bot, update):
    """Method used to start the automaton"""
    reply_keyboard = [['Español 🇪🇸', 'English 🇬🇧']]
    update.message.reply_markdown('🇬🇧 🇪🇸 ?',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    logger.info('%s started the bot.', update.message.from_user.first_name)
    return LANGUAGE


def language_selected(bot, update):
    """Select introduction based on first selection. Can be changed if the user uses the command of the other introduction"""
    mssg = update.message
    if pattern.match(mssg.text):
        update.message.reply_markdown(en_str.language1 +
                                      mssg.from_user.first_name + '.',
                                      reply_markup=ReplyKeyboardRemove())
        update.message.reply_markdown(en_str.language2)
        update.message.reply_markdown(en_str.language3)
        return MODE_SELECTION
    else:
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
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ayuda', ayuda))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document, test))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        allow_reentry=True,

        states={
            LANGUAGE: [MessageHandler(Filters.text, language_selected)],

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

import strings_es as es_str
import Teletutor_bot
import logging
from telegram import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
LANGUAGE, MODE_SELECTION, GUIDE, MESSAGES, GROUPS, CHANNELS, CLOUD, BOTS, MEDIA, SECRET_CHATS = range(10)


def ayuda(bot, update):
    update.message.reply_text(es_str.help)


def stop_es(bot, update):
    """Ends the automaton"""
    logger.info('%s stopped the bot', update.message.from_user.first_name)
    update.message.reply_markdown(es_str.forced_end)
    return Teletutor_bot.ConversationHandler.END


def language_es(bot, update):
    mssg = update.message
    update.message.reply_markdown(es_str.introduction +
                                  mssg.from_user.first_name + '.',
                                  reply_markup=ReplyKeyboardRemove())
    update.message.reply_markdown(es_str.select_mode)
    return MODE_SELECTION


def tutorial_es(bot, update):
    return messages_es(bot, update)


def messages_es(bot, update):
    """Send information about messages"""
    update.message.reply_markdown(es_str.messages)
    update.message.reply_markdown(es_str.nextsection)
    return GROUPS


def groups_es(bot, update):
    """Send information about groups"""
    update.message.reply_markdown(es_str.groups)
    update.message.reply_markdown(es_str.nextsection)
    return CHANNELS


def channels_es(bot, update):
    """Send information about channels"""
    update.message.reply_markdown(es_str.channels)
    update.message.reply_markdown(es_str.nextsection)
    return CLOUD


def cloud_es(bot, update):
    """Send information about cloud storage"""
    update.message.reply_markdown(es_str.cloud)
    update.message.reply_markdown(es_str.nextsection)
    return BOTS


def bots_es(bot, update):
    """Send information about Bbts"""
    update.message.reply_markdown(es_str.bots)
    update.message.reply_markdown(es_str.bots2)
    return MEDIA


def media_es(bot, update):
    """Checks if sent message was a gif from @gif bot"""
    if update.message.document:
        if update.message.document.file_name == 'giphy.mp4':
            update.message.reply_markdown(es_str.media)
            update.message.reply_markdown(es_str.media2)
            return SECRET_CHATS
        elif update.message.document.mime_type == 'video/mp4':
            update.message.reply_markdown(es_str.media_error1)
        else:
            update.message.reply_markdown(es_str.media_error2)


def secret_chats_es(bot, update):
    """Send information about secret chats"""
    update.message.reply_markdown(es_str.secret_chats)
    update.message.reply_markdown(es_str.end)
    return Teletutor_bot.ConversationHandler.END

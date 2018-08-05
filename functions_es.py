import logging

import Teletutor_bot
from telegram.ext import *
import settings as st

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()


def ayuda(bot, update):
    update.message.reply_text(st.strings["help"])


def stop_es(bot, update):
    """Ends the automaton"""
    logger.info('%s (@%s) stopped the bot', update.message.from_user.first_name, update.message.chat.username)
    update.message.reply_markdown(st.strings["force_end"])
    return Teletutor_bot.ConversationHandler.END


def error(bot, update):
    """Notify the user that his message wasn't expected by the automaton."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    update.message.reply_markdown(st.strings["error"])


def start_es(bot, update):
    mssg = update.message
    update.message.reply_markdown(st.strings["introduction"])
    update.message.reply_markdown(st.strings["select_mode"])
    logger.info('%s (@%s) started the bot', update.message.chat.first_name, update.message.chat.username)


def tutorial_es(bot, update):
    logger.info('%s (@%s) started tutorial mode', update.message.chat.first_name,
                update.message.chat.username)
    return messages_es(bot, update)


def messages_es(bot, update):
    """Send information about messages"""
    update.message.reply_markdown(st.strings["messages"])
    update.message.reply_markdown(st.strings["next-section"])
    return st.GROUPS


def groups_es(bot, update):
    """Send information about groups"""
    update.message.reply_markdown(st.strings["groups"])
    update.message.reply_markdown(st.strings["next-section"])
    return st.CHANNELS


def channels_es(bot, update):
    """Send information about channels"""
    update.message.reply_markdown(st.strings["channels"])
    update.message.reply_markdown(st.strings["next-section"])
    return st.CLOUD


def cloud_es(bot, update):
    """Send information about cloud storage"""
    update.message.reply_markdown(st.strings["cloud"])
    update.message.reply_markdown(st.strings["next-section"])
    return st.BOTS


def bots_es(bot, update):
    """Send information about Bots"""
    update.message.reply_markdown(st.strings["bots"])
    update.message.reply_markdown(st.strings["bots2"])
    return st.MEDIA


def media_es(bot, update):
    """Checks if sent message was a gif from @gif bot"""
    if update.message.document:
        if update.message.document.file_name == 'giphy.mp4':
            update.message.reply_markdown(st.strings["media"])
            update.message.reply_markdown(st.strings["media2"])
            return st.CHAT_PREVIEW
        elif update.message.document.mime_type == 'video/mp4':
            update.message.reply_markdown(st.strings["media_error1"])
        else:
            update.message.reply_markdown(st.strings["media_error2"])


def chat_preview_es(bot, update):
    """Send information about secret chats"""
    update.message.reply_markdown(st.strings["chat_preview"])
    update.message.reply_markdown(st.strings["next-section"])
    return st.VIDEO_NOTES


def video_notes_es(bot, update):
    """Send information about secret chats"""
    update.message.reply_markdown(st.strings["video_notes"])
    update.message.reply_markdown(st.strings["video_notes2"])
    return st.SECRET_CHATS


def secret_chats_es(bot, update):
    """Send information about secret chats"""
    if update.message.video_note:
        update.message.reply_markdown(st.strings["secret_chats"])
        update.message.reply_markdown(st.strings["end_tutorial"])
        return ConversationHandler.END
    else:
        update.message.reply_markdown(st.string["video_note_error"])

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import settings as st

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

keyboard_guia_es = [[InlineKeyboardButton("Mensajes", callback_data='messages'),
                     InlineKeyboardButton("Grupos", callback_data='groups')],
                    [InlineKeyboardButton("Canales", callback_data='channels'),
                     InlineKeyboardButton("Nube", callback_data='cloud')],
                    [InlineKeyboardButton("Bots", callback_data='bots'),
                     InlineKeyboardButton("Multimedia", callback_data='media')],
                    [InlineKeyboardButton("Chat Preview", callback_data='chat_preview'),
                     InlineKeyboardButton("Notas de video", callback_data="video_notes")],
                     [InlineKeyboardButton("Chats secretos", callback_data='secret_chats')]]
reply_markup_guide = InlineKeyboardMarkup(keyboard_guia_es)


def guide_es(bot, update):
    update.message.reply_text(st.strings["selection"], reply_markup=reply_markup_guide)
    logger.info('%s (@%s) started guide mode', update.message.chat.first_name,
                update.message.chat.username)
    return st.GUIDE


def button_guide(bot, update):
    """The program read the callback_query and send the appropriate section"""
    query = update.callback_query
    data = query.data
    logger.info('%s (@%s) selected %s', update.callback_query.message.chat.first_name,
                update.callback_query.message.chat.username, data)

    # We notify that have receive the callback and reply.
    bot.answer_callback_query(update.callback_query.id)
    bot.edit_message_text(text=st.strings[data],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup_guide,
                          parse_mode=ParseMode.MARKDOWN)

import logging
import settings as st
from telegram import *

import strings_es as es_str

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

keyboard_guia_es = [[InlineKeyboardButton("Mensajes", callback_data='messages'),
                     InlineKeyboardButton("Grupos", callback_data='groups')],
                    [InlineKeyboardButton("Canales", callback_data='channels'),
                     InlineKeyboardButton("Nube", callback_data='cloud')],
                    [InlineKeyboardButton("Bots", callback_data='bots'),
                     InlineKeyboardButton("Multimedia", callback_data='media')],
                    [InlineKeyboardButton("Chats secretos", callback_data='secret_chats')]]
reply_markup_guide = InlineKeyboardMarkup(keyboard_guia_es)


def guide_es(bot, update):
    update.message.reply_text(es_str.selection, reply_markup=reply_markup_guide)
    return st.GUIDE


def button_guide(bot, update):
    query = update.callback_query
    data = query.data
    logger.info('%s selected %s',
                update.callback_query.message.chat.first_name,
                data)
    bot.edit_message_text(text=getattr(es_str, data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup_guide,
                          parse_mode=ParseMode.MARKDOWN)

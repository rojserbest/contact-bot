from telegram.ext import CallbackContext, MessageHandler, Filters
from telegram import Update

from config import CHAT_FILTER


def reply(update: Update, context: CallbackContext) -> None:
    message_ = update.message.reply_to_message

    if message_.from_user.id == context.bot.id:
        chat_id_ = message_.forward_from.id if message_.forward_from else message_.entities[0].url.split(
            "/")[-1]
        update.message.copy(chat_id_)


__handlers__ = [
    [
        MessageHandler(
            Filters.reply & CHAT_FILTER
            & ~ Filters.command,
            reply
        )
    ],
]

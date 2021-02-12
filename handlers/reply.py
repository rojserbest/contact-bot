from telegram.ext import MessageHandler, Filters

from config import CHAT_FILTER


def reply(update, context):
    message_ = update.message.reply_to_message

    if message_.from_user.id == context.bot.id:
        chat_id_ = message_.forward_from.id if message_.forward_from else message_.entities[0].url.split(
            "/")[-1]
        update.message.copy(chat_id_)


__handlers__ = [
    [
        MessageHandler(Filters.reply & CHAT_FILTER &
                       ~ Filters.command, reply)
    ],
]

from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users


@not_banned_users
def message(update, context):
    message_ = update.message.forward(-1001243271409)

    if not message_.forward_from:
        context.bot.send_message(-1001243271409,
                                 f"<a href=\"http://127.0.0.1/{update.message.from_user.id}\">\xad</a>Reply to this message.", parse_mode="HTML", reply_to_message_id=message_.message_id)


__handlers__ = [
    [
        MessageHandler(Filters.all & Filters.chat_type.private &
                       ~ Filters.command, message)
    ],
]

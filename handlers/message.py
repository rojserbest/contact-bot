from telegram.ext import CallbackContext, MessageHandler, Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users


@not_banned_users
def message(update: Update, context: CallbackContext) -> None:
    message_ = update.message.forward(-1001243271409)

    if not message_.forward_from:
        message_.reply_text(
            f"<a href=\"http://127.0.0.1/{update.message.from_user.id}\">\xad</a>Reply to this message.", parse_mode="HTML")


__handlers__ = [
    [
        MessageHandler(Filters.all & Filters.chat_type.private &
                       ~ Filters.command, message)
    ],
]

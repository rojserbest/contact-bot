from telegram.ext import CommandHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users
from strings import get_string, get_languages


@not_banned_users
def start(update, context):
    buttons = []

    for language in get_languages():
        if language != context.bot_data.get(update.message.chat.id, {}).get("lang", "en"):
            buttons.append(
                InlineKeyboardButton(
                    get_languages()[language],
                    callback_data="setlang_" + language
                )
            )

    keyboard = [buttons]

    update.effective_message.reply_text(
        get_string("start", context.chat_data.get("lang")),
        reply_markup=InlineKeyboardMarkup(
            keyboard) if keyboard != [[]] else None
    )


__handlers__ = [
    [
        CommandHandler("start", start, filters=Filters.private)
    ]
]

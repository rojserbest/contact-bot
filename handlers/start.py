from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users
from strings import get_string, get_languages, lang_


@not_banned_users
@lang_
def start(update: Update, context: CallbackContext, lang: str):
    keyboard = []

    for language in get_languages():
        if language != lang:
            keyboard.append(
                [
                    InlineKeyboardButton(
                        get_languages()[language],
                        callback_data="setlang_" + language
                    )
                ]
            )

    update.effective_message.reply_text(
        get_string("start", lang),
        reply_markup=InlineKeyboardMarkup(
            keyboard
        ) if keyboard != [[]] else None
    )


__handlers__ = [
    [
        CommandHandler("start", start, filters=Filters.chat_type.private)
    ]
]

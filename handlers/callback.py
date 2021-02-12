from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users
from strings import get_string, get_languages


@not_banned_users
def set_lang(update, context):
    context.bot_data[update.effective_chat.id]["lang"] = update.callback_query.split(
        "_")[-1]
    update.effective_message.delete()

    keyboard = []

    for language in get_languages():
        if language != context.bot_data.get(update.message.chat.id, {}).get("lang", "en"):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        get_languages()[language],
                        callback_data="setlang_" + language
                    )
                ]
            )

    context.bot.send_message(
        update.effective_chat.id,
        get_string("start", context.chat_data.get("lang")),
        reply_markup=InlineKeyboardMarkup(
            keyboard) if keyboard != [[]] else None
    )


__handlers__ = [
    [
        CallbackQueryHandler(set_lang, pattern="setlang.+")
    ]
]

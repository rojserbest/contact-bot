from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from .ban import not_banned_users
from strings import get_string, get_languages, _lang


@not_banned_users
def set_lang(update: Update, context: CallbackContext) -> None:
    lang = update.callback_query.data.split("_")[-1]

    if update.effective_chat.id in context.bot_data:
        context.bot_data[update.effective_chat.id]["lang"] = lang
    else:
        context.bot_data[update.effective_chat.id] = dict(lang=lang)

    update.effective_message.delete()

    keyboard = []

    for language in get_languages():
        if language != context.bot_data.get(update.effective_chat.id, {}).get("lang", "en"):
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
        get_string(
            "start",
            _lang(context, update.effective_chat.id)
        ),
        reply_markup=InlineKeyboardMarkup(keyboard)
        if keyboard != [[]] else None
    )

    update.callback_query.answer()


__handlers__ = [
    [
        CallbackQueryHandler(set_lang, pattern="setlang_.+")
    ]
]

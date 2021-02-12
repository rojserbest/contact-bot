from telegram.ext import CallbackContext

from .string import strings

get_string = strings.get_string
get_languages = strings.get_languages


def lang_(func):
    def wrapper(update, context):
        return func(
            update,
            context,
            context.bot_data.get(
                update.effective_chat.id, {}
            ).get(
                "lang", "en"
            )
        )
    return wrapper


def _lang(context: CallbackContext, chat_id: int):
    return context.bot_data.get(
        chat_id, {}
    ).get(
        "lang", "en"
    )

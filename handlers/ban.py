from telegram.ext import CommandHandler

from database import bans as db
from strings import get_string
from config import CHAT_FILTER


def ban(update, context):
    message_ = update.message.reply_to_message

    if message_.from_user.id == context.bot.id:
        chat_id_ = message_.forward_from.id if message_.forward_from else message_.entities[0].url.split(
            "/")[-1]

        if db.is_banned(chat_id_):
            update.message.reply_text("This person is already banned.")
            return

        db.ban(chat_id_)

        context.bot.send_message(
            chat_id_, get_string(
                "ban",
                context.bot_data.get(
                    chat_id_, {}
                ).get(
                    "lang",
                    "en"
                )
            )
        )

        update.message.reply_text("Banned.")


def unban(update, context):
    message_ = update.message.reply_to_message

    if message_.from_user.id == context.bot.id:
        chat_id_ = message_.forward_from.id if message_.forward_from else message_.entities[0].url.split(
            "/")[-1]

        if db.is_banned(chat_id_):
            db.unban(chat_id_)

        context.bot.send_message(
            chat_id_, get_string(
                "unban",
                context.bot_data.get(
                    chat_id_, {}
                ).get(
                    "lang",
                    "en"
                )
            )
        )

        update.message.reply_text("Unbanned.")


def not_banned_users(func):
    def wrapper(update, context):
        if not db.is_banned(update.message.from_user.id):
            return func(update, context)
    return wrapper


__handlers__ = [
    [
        CommandHandler("ban", ban, filters=CHAT_FILTER)
    ],
    [
        CommandHandler("unban", unban, filters=CHAT_FILTER)
    ],
]

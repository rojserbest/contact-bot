from telegram.ext import CallbackContext, CommandHandler
from telegram import Update

from database import bans as db
from strings import get_string, _lang
from config import CHAT_FILTER


def ban(update: Update, context: CallbackContext) -> None:
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
                _lang(context, chat_id_)
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
                _lang(context, chat_id_)
            )
        )

        update.message.reply_text("Unbanned.")


def not_banned_users(func):
    def wrapper(update, context):
        if not db.is_banned(update.effective_user.id):
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

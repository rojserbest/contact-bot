"""
A simple Pyrogram bot 
which lets it's users 
contact a group of people 
without needing to 
create a special group for it.


Written by: @rojserbest.
"""

from os import getenv
import html

from pyrogram import Client, filters, idle
from dotenv import load_dotenv

load_dotenv()

bot = Client(
    "contact_bot",
    int(getenv("API_ID")),
    getenv("API_HASH"),
    bot_token=getenv("BOT_TOKEN")
)
bot.start()

bot_id = bot.get_me().id
group = int(getenv("GROUP"))
from_group = filters.chat(group)
last_sender_id = 1


def get_id_from_text(text):
    text = str(text)

    try:
        return int(text.split("[")[-1][:-2])
    except:
        return None


@bot.on_message(filters.private & filters.command("start"))
def ___(__, _):
    _.reply_text("I am alive, you can send messages to contact!")


@bot.on_message(filters.private & ~ filters.command("start"))
def ____(__, _):
    global last_sender_id

    sender_id = _.from_user.id

    if last_sender_id != sender_id:
        last_sender_id = sender_id
        sender_name = html.escape(
            "{}{}".format(
                _.from_user.first_name,
                f" {_.from_user.last_name}" if _.from_user.last_name else ""
            )
        )
        sender_username = "{}".format(
            f" @{_.from_user.username}" if _.from_user.username else ""
        )
        __.send_message(
            group,
            f"{sender_name}{sender_username} [`{sender_id}`]:"
        )

    try:
        _.forward(group)
    except:
        __.send_message(group, "Could not forward message.")


@bot.on_message(filters.reply & from_group)
def _____(__, _):
    _r = _.reply_to_message

    if _r.from_user.id != bot_id:
        return

    user = get_id_from_text(_r.text)

    if not user:
        _.reply("Reply to a message which contains a user id.")
    else:
        try:
            _.copy(user)
        except:
            _.reply("Could not send the message.")


idle()

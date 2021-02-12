
from os import getenv

from dotenv import load_dotenv
from telegram.ext import Filters

load_dotenv()

CHAT_ID = int(getenv("CHAT_ID"))
BOT_TOKEN = getenv("BOT_TOKEN")
DB_URI = getenv("DB_URI")


CHAT_FILTER = Filters.chat(CHAT_ID)

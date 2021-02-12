from telegram.ext import Updater, PicklePersistence

from config import BOT_TOKEN

updater = Updater(
    BOT_TOKEN,
    persistence=PicklePersistence(filename="data")
)
dp = updater.dispatcher


def main():
    from handlers import all_handlers

    for handler in all_handlers:
        if len(handler) == 2:
            if handler[0] == "error":
                dp.add_error_handler(
                    handler[1]
                )
            else:
                dp.add_handler(
                    handler[0],
                    handler[1]
                )
        else:
            dp.add_handler(
                handler[0]
            )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

import logging
from bot import bot

if __name__ == "__main__":
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as exception:
        logging.info("The bot crashed with an error s%", exception)
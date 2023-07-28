import os

from dotenv import load_dotenv
from telebot import TeleBot
import config
import handlers.commands_handler
import handlers.callback_handler

load_dotenv()
bot = TeleBot(os.getenv("BOT_TOKEN"), "HTML")

handlers.commands_handler.init_bot(bot)
handlers.callback_handler.init_bot(bot)
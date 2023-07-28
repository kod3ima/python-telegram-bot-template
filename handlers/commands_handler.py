import os

from telebot import TeleBot

from utils.localization_util import Localization
from utils.scan_dir_util import get_directory_tree

def init_bot(bot: TeleBot):
    localization = Localization("locales/ru/translates.yaml")

    @bot.message_handler(commands=["start"])
    def command_start(message):
        return bot.send_message(message.chat.id, localization.get("greeting"))
import json

from telebot import TeleBot

from utils.localization_util import Localization

def init_bot(bot: TeleBot):
    localization  = Localization("locales/ru/translates.yaml")
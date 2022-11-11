from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Subscription')
    b2 = KeyboardButton(text='Catalog')
    b3 = KeyboardButton(text='Tracking')
    b4 = KeyboardButton(text='Send massage')
    b5 = KeyboardButton(text='Help')
    b6 = KeyboardButton(text='Channels')
    kb.add(b1).add(b2, b3).add(b4).add(b5, b6)
    return kb


def get_kb_sub() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(resize_keyboard=True)
    ib1 = InlineKeyboardButton(text='Sub', callback_data='Sub')
    ib2 = InlineKeyboardButton(text='Cancel', callback_data='Cancel')
    ikb.add(ib1).add(ib2)
    return ikb

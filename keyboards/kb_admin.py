from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    b1 = KeyboardButton(text='New photo')
    kb.add(b1)
    return kb


def get_kb_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Cancel')
    kb.add(b1)
    return kb


def get_kb2_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Next')
    b2 = KeyboardButton(text='Cancel')
    kb.add(b1).add(b2)
    return kb


def get_kb3_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Dog')
    b2 = KeyboardButton(text='Cat')
    b3 = KeyboardButton(text='Car')
    b4 = KeyboardButton(text='Cancel')
    kb.add(b1, b2, b3).add(b4)
    return kb

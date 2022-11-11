from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # b1 = KeyboardButton(text='Каталог')
    # b2 = KeyboardButton(text='Поиск по каталогу')
    b1 = KeyboardButton(text='New photo')
    # b4 = KeyboardButton(text='Товары ожидающие публикации')
    # b5 = KeyboardButton(text='Помощь')
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
    b1 = KeyboardButton(text='Private')
    b2 = KeyboardButton(text='Life')
    b3 = KeyboardButton(text='Erotic')
    b4 = KeyboardButton(text='Cancel')
    kb.add(b1, b2, b3).add(b4)
    return kb



def get_ikb_availability() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib1 = InlineKeyboardButton(text='Да', callback_data='yes')
    ib2 = InlineKeyboardButton(text='Нет', callback_data='no')
    ikb.add(ib1, ib2)
    return ikb


def get_ikb_catalog() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text='Редактировать', callback_data='product_edit')
    ib2 = InlineKeyboardButton(text='Удалить', callback_data='product_delete')
    ib3 = InlineKeyboardButton(text='Скрыть', callback_data='product_hide')
    ikb.add(ib1, ib2, ib3)
    return ikb


def get_ikb_edit() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text='Название', callback_data='edit_name_product')
    ib2 = InlineKeyboardButton(text='Цена', callback_data='edit_price')
    ib3 = InlineKeyboardButton(text='Описание', callback_data='edit_description')
    ib4 = InlineKeyboardButton(text='Публикация', callback_data='edit_availability')
    ib5 = InlineKeyboardButton(text='Закончить редактирование', callback_data='edit_cancel')
    ikb.add(ib1, ib2, ib3, ib4, ib5)
    return ikb

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from data_base import data_base
import datetime
from keyboards import kb_client


# @dp.message_handler(commands=['start'], is_admin=False, state=None)
async def command_start(message: types.Message) -> None:

    if message.from_user.id not in await data_base.data_user():
        await data_base.add_user(message.from_user.id,
                                 message.from_user.first_name,
                                 datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello, {message.from_user.first_name}!',
                           reply_markup=kb_client.get_kb_start())
    await message.delete()


# @dp.message_handler(Text(equals='Subscription', ignore_case=True), is_admin=False, state=None)
async def command_subscription(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Here you can subscribe',
                           reply_markup=kb_client.get_kb_sub())


# @dp.callback_query_handler('Sub', is_admin=False)
async def callback_sub(callback: types.CallbackQuery) -> None:
    await callback.answer(text="So good!")


def register_handlers_client(dp: Dispatcher) -> None:
    dp.register_message_handler(command_start,
                                commands=['start'],
                                is_admin=False,
                                state=None)
    dp.register_message_handler(command_subscription,
                                Text(equals='Subscription', ignore_case=True),
                                is_admin=False,
                                state=None)
    dp.register_callback_query_handler(callback_sub,
                                       lambda callback: callback.data.startswith('Sub'),
                                       is_admin=False)
    

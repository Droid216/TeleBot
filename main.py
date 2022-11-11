from aiogram import executor
from create_bot import dp

from handlers import client, admin, other
from data_base import data_base
from filter import admin_filter


async def on_startup(_) -> None:
    print('Start bot')
    data_base.sql_start()


if __name__ == '__main__':
    admin_filter.register_filter(dp)
    admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

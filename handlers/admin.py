from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_admin
from data_base import data_base
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class CreationPhotoPack(StatesGroup):
    name = State()
    price = State()
    caption = State()
    photo_title = State()
    gallery = State()
    type_pack = State()


class EditProduct(StatesGroup):
    product_name = State()
    photo = State()
    price = State()
    description = State()
    availability = State()


class SearchProduct(StatesGroup):
    search = State()

print([state for state in CreationPhotoPack.states_names if state != CreationPhotoPack.caption.state])
# @dp.message_handler(is_admin=True, commands=['start'], state=None)
async def cmd_start_admin(message: types.Message) -> None:
    await message.answer(text='Hello, admin',
                         reply_markup=kb_admin.get_kb_start())


# @dp.message_handler(Text(equals='Помощь', ignore_case=True), is_admin=True, state=None)
async def help_admin_handler(message: types.Message) -> None:
    text = '''
    <b>/start</b> - <em>начало работы бота</em>
    <b>Каталог</b> - <em>вызов каталога опубликованных товаров</em>
    <b>Добавить товар</b> - <em>начало процессса добавления товара в каталог</em>
    <b>Товары ожидающие публикации</b> - <em>вызов каталога ожидающих публикации товаров</em>
    <b>Помощь</b> - <em>вызов подсказки по командам бота</em>
    '''
    await message.answer(text=text,
                         parse_mode='HTML')


# @dp.message_handler(Text(equals='Каталог', ignore_case=True), is_admin=True, state=None)
async def catalog_admin_handler(message: types.Message) -> None:
    for product in await data_base.sql_read_catalog():
        if product['availability']:
            text = f'{product["product_name"]}\nЦена: {product["price"]} руб.\n{product["description"]}'
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=product['photo'],
                                 caption=text,
                                 reply_markup=kb_admin.get_ikb_catalog())


# @dp.message_handler(Text(equals='Cancel', ignore_case=True), is_admin=True, state='*')
async def cancel_admin_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text='Process interrupted',
                         reply_markup=kb_admin.get_kb_start())


# @dp.message_handler(Text(equals='New photo', ignore_case=True), is_admin=True, state=None)
async def new_photo_handler(message: types.Message) -> None:
    await CreationPhotoPack.name.set()
    await message.answer(text='Input title package photo',
                         reply_markup=kb_admin.get_kb_cancel())


# @dp.message_handler(is_admin=True, state=CreationPhotoPack.name)
async def load_name_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
    await CreationPhotoPack.next()
    await message.answer(text='Input price',
                         reply_markup=kb_admin.get_kb_cancel())


# @dp.message_handler(is_admin=True, state=CreationPhotoPack.price)
async def load_price_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['price'] = message.text
    await CreationPhotoPack.next()
    await message.answer(text='Input caption',
                         reply_markup=kb_admin.get_kb_cancel())


# @dp.message_handler(is_admin=True, state=CreationPhotoPack.caption)
async def caption_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['caption'] = message.text
    await CreationPhotoPack.next()
    await message.answer(text='Loading title photo',
                         reply_markup=kb_admin.get_kb_cancel())


# @dp.message_handler(is_admin=True, content_types=['photo'], state=CreationPhotoPack.photo_title)
async def photo_title_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo_title'] = message.photo[0].file_id
    await CreationPhotoPack.next()
    async with state.proxy() as data:
        data['gallery'] = ''
    await message.answer(text='Load package photo',
                         reply_markup=kb_admin.get_kb2_cancel())


# @dp.message_handler(is_admin=True, content_types=['photo'], state=CreationPhotoPack.gallery)
async def gallery_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        if data['gallery']:
            data['gallery'] += ', ' + message.photo[0].file_id
        else:
            data['gallery'] += message.photo[0].file_id
    await message.answer(text='Load next photo',
                         reply_markup=kb_admin.get_kb2_cancel())


# @dp.message_handler(Text(equals='Next', ignore_case=True), is_admin=True, state=CreationPhotoPack.gallery)
async def gallery_next_handler(message: types.Message, state: FSMContext) -> None:
    await CreationPhotoPack.next()
    await message.answer(text='Select photo type',
                         reply_markup=kb_admin.get_kb3_cancel())


# @dp.message_handler(Text(contains=['Private', 'Life', 'Erotic']), is_admin=True, state=CreationPhotoPack.type_pack)
async def type_photo_handler(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['type_pack'] = message.text
    await data_base.add_photo(state)
    await state.finish()
    await message.answer(text='Photo pack created',
                         reply_markup=kb_admin.get_kb_start())


def register_handlers_admin(dp: Dispatcher) -> None:

    dp.register_message_handler(cmd_start_admin,
                                is_admin=True,
                                commands=['start'],
                                state=None)
    dp.register_message_handler(cancel_admin_handler,
                                Text(equals='Cancel', ignore_case=True),
                                is_admin=True,
                                state=[state for state in CreationPhotoPack.states_names if state != CreationPhotoPack.caption.state])
    dp.register_message_handler(new_photo_handler,
                                Text(equals='New photo', ignore_case=True),
                                is_admin=True,
                                state=None)
    dp.register_message_handler(load_name_handler,
                                is_admin=True,
                                state=CreationPhotoPack.name)
    dp.register_message_handler(load_price_handler,
                                is_admin=True,
                                state=CreationPhotoPack.price)
    dp.register_message_handler(caption_handler,
                                is_admin=True,
                                state=CreationPhotoPack.caption)
    dp.register_message_handler(photo_title_handler,
                                content_types=['photo'],
                                is_admin=True,
                                state=CreationPhotoPack.photo_title)
    dp.register_message_handler(gallery_handler,
                                content_types=['photo'],
                                is_admin=True,
                                state=CreationPhotoPack.gallery)
    dp.register_message_handler(gallery_next_handler,
                                Text(equals='Next', ignore_case=True),
                                is_admin=True,
                                state=CreationPhotoPack.gallery)
    dp.register_message_handler(type_photo_handler,
                                is_admin=True,
                                state=CreationPhotoPack.type_pack)

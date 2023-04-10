from aiogram import types
from config import dp
from classes.init import bd


@dp.message_handler(commands=['show'])
async def show(message: types.Message):
    bd.fill_data(message.from_user.id)
    res = bd.show(message.from_user.id)
    if res:
        await message.answer('<b>Список всех событий:</b>\n\n' + res + '\n/list – список команд', parse_mode='HTML')
    else:
        await message.answer('Список пуст.')
    bd.clear(message.from_user.id)
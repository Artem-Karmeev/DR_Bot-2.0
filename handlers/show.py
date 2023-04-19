from aiogram import types
from config import dp
from classes.database import UserData as us


@dp.message_handler(commands=['show'])
async def show(message: types.Message):

    data = us(message, load_events = True).show()
    if data:
        await message.answer(f'<b>Список всех событий:</b>\n\n{data}\n', parse_mode='HTML')
    else:
        await message.answer('Список пуст.')
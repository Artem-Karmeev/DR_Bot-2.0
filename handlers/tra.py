from aiogram import types
from config import dp


@dp.message_handler()
async def func(message: types.Message):
    await message.answer('Не понял, повтори:')
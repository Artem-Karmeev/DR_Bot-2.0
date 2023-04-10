from aiogram.dispatcher import FSMContext
from aiogram import types
from config import dp
from classes.init import bd
from text import list_command


@dp.message_handler(commands=['back'], state="*")
async def back(message: types.Message, state: FSMContext):
    try:
        bd.clear(message.from_user.id)
        await message.answer(list_command)
        await state.finish()
    except Exception:
        await message.answer("ERROR")
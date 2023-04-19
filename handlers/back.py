from aiogram.dispatcher import FSMContext
from aiogram import types
from config import dp


@dp.message_handler(commands=['back'], state="*")
async def back(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except Exception:
        await message.answer("ERROR")
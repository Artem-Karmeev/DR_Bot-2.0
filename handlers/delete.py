from aiogram import types
from config import dp
from classes.database import UserData as us
from aiogram.dispatcher import FSMContext
from classes.fsm import UserStatus


@dp.message_handler(commands=['del'])
async def my_del_1(message: types.Message):
    await UserStatus.delete.set()
    await message.answer('Введи 🆔 события, чтобы его удалить:')


@dp.message_handler(state=UserStatus.delete)
async def my_del_2(message: types.Message, state: FSMContext):

    if message.text.strip().isdigit():
        text = us(message, load_events=True).del_event(int(message.text.strip()))
        await message.answer(text)
    else:
        await message.answer('ERROR')
    await state.finish()
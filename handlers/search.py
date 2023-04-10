from aiogram import types
from config import dp
from classes.init import bd
from aiogram.dispatcher import FSMContext
from classes.fsm import UserStatus

@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    await UserStatus.search.set()
    await message.answer('Введи искомое значение:')


@dp.message_handler(state=UserStatus.search)
async def search_2(message: types.Message, state: FSMContext):
    bd.fill_data(message.from_user.id)
    result = bd.search(message.from_user.id, message.text.lower())
    if result:
        await message.answer(result.strip() + '\n\n/list – список команд ')
    else:
        await message.answer('Совпадений нет, возможно список пуст.\n\n/list – список команд')
    bd.clear(message.from_user.id)
    await state.finish()
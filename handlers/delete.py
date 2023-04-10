from aiogram import types
from config import dp
from classes.init import bd
from aiogram.dispatcher import FSMContext
from classes.fsm import UserStatus

@dp.message_handler(commands=['del'])
async def search(message: types.Message):
    await UserStatus.delete.set()
    await message.answer('Введи 🆔 события, чтобы его удалить:\n\n/back - Вернуться назад')


@dp.message_handler(state=UserStatus.delete)
async def search_2(message: types.Message, state: FSMContext):
    bd.fill_data(message.from_user.id)
    my_len = bd.len(message.from_user.id)
    if message.text.strip().isdigit():
        if -1 < int(message.text.strip()) < my_len:
            bd.del_event(message.from_user.id, int(message.text.strip()))
            await message.answer('Событие удалено.\n/list - Список команд')
        else:
            await message.answer('ERROR')
    else:
        await message.answer('ERROR')
    bd.clear(message.from_user.id)
    await state.finish()
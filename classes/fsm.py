from aiogram.dispatcher.filters.state import StatesGroup, State

class UserStatus(StatesGroup):

    add_date = State()
    add_comment = State()

    delete = State()
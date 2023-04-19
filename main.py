from aiogram import executor
from aiogram.types import BotCommand
from handlers import dp
from config import bot


async def on_start(_):
    print('Hello!')
    
    bot_commands = [ 
        BotCommand(command='/add', description='Добавить событие'),
        BotCommand(command='/show', description='Показать все события'),
        BotCommand(command='/del', description='Удалить событие'),
        BotCommand(command='/back', description='Отмена действия'),
        BotCommand(command='/switch', description=f'Управление уведомлениями')
    ]
    await bot.set_my_commands(bot_commands)


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True, on_startup=on_start)
from aiogram import Dispatcher, types


async def cmd_start(msg: types.Message):
    await msg.answer('Привет, добро пожаловать, пока')


async def cmd_menu(msg: types.Message):
    await msg.answer('Список команд:\n')


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_menu, commands='menu')

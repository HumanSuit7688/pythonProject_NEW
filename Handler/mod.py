from aiogram import Dispatcher, types
from Modules.parther import lottery


async def cmd_lottery(msg: types.Message):
    a = msg.get_args()
    x = lottery(int(a))
    if x == True:
        await msg.answer('Победа вместо обеда')
    else:
        await msg.answer('нт, в другой раз получится')


def register_handlers_mod(dp: Dispatcher):
    dp.register_message_handler(cmd_lottery, commands='lot')
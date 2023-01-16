import config
import asyncio
from aiogram import Bot, Dispatcher, types
from Handler.start import register_handlers_start
from Handler.mod import register_handlers_mod

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def main():
    register_handlers_mod(dp)
    register_handlers_start(dp)
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())

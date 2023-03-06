import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from background import keep_alive

openai.api_key = "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"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(
        "Привет, я помогу тебе использовать всеми известную нейросеть'ChatGPT' прямо в этом чате. Тебе нужно просто написать сообщение без всяких команд, и это будет запросом к нейросети.\nИногда бот долго отвечает из-за того что программа ообрабатывает много запросов по цепочке. Если не отвечает более 2-3 минут, да и по всем вопросам пиши разработчику - https://t.me/HumanSuit8\nПользуйся!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(
        "Я помогу тебе использовать всеми известную нейросеть'ChatGPT' прямо в этом чате. Тебе нужно просто написать сообщение без всяких команд, и это будет запросом к нейросети.\nИногда бот долго отвечает из-за того что программа ообрабатывает много запросов по цепочке. Если бот не отвечает более 2-3 минут, да и вообще по любым вопросам пиши разработчику - https://t.me/HumanSuit8\nПользуйся!")


@dp.message_handler()
async def gpt_request_message(msg: types.Message):
    try:
        # задаем модель и промпт
        model_engine = "text-davinci-003"
        prompt = msg.text

        # задаем макс кол-во слов
        max_tokens = 1024

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1536,
            temperature=0.3,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = completion.choices[0].text
        await msg.answer(answer)
    except:
        pass


if __name__ == '__main__':
    keep_alive()
    executor.start_polling(dp)

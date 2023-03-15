import openai
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from config2 import TOKEN
# from background import keep_alive

openai.api_key = "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"

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

response = openai.Image.create(
  prompt="a red car, which is riding very fast, realistic, neon color",
  n=2,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

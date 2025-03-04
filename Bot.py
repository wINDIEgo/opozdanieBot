import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import F
import asyncio

# Замените 'YOUR_BOT_TOKEN' на свой токен
TOKEN = "7675171655:AAFA4itTlQo7GIEAVsypGpEQt-zXg6z-BFA"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список оправданий
excuses = [
    "Извините, я опоздал, потому что разговаривал с котом о смысле жизни.",
    "Пробки? Нет, просто завис, думая о том, как голуби управляют миром.",
    "Я не опоздал, это мир слишком рано начал.",
    "Моя собака съела будильник. Буквально.",
    "Я забыл, что нужно выходить из дома, чтобы куда-то прийти."
]

@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.reply("Привет! Я бот, который поможет тебе оправдаться за опоздание. Напиши /оправдание и я придумаю что-то гениальное!")

@dp.message(F.text == "/оправдание")
async def send_excuse(message: Message):
    excuse = random.choice(excuses)
    await message.reply(excuse)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
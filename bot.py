import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8956006401:AAEUArB7IsF-ceqJoaTyOajUC_XMdLJ3s2M"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Добро пожаловать в KRaks Store\n\n"
        "💎 MAGIC для OXIDE\n"
        "💰 Цена: 280₽ / 1 день\n\n"
        "📞 Поддержка: @No_Fake_Kraks"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
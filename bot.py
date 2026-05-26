import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

TOKEN = "8956006401:AAEUArB7IsF-ceqJoaTyOajUC_XMdLJ3s2M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💎 Купить")],
        [KeyboardButton(text="📦 Тарифы")],
        [KeyboardButton(text="📞 Поддержка")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 KRaks Store\n\n"
        "💎 MAGIC для OXIDE",
        reply_markup=keyboard
    )

@dp.message()
async def buttons(message: Message):

    if message.text == "📦 Тарифы":
        await message.answer(
            "📦 Тарифы:\n\n"
            "💎 1 День — 280₽"
        )

    elif message.text == "💎 Купить":
        await message.answer(
            "📞 Для покупки: @No_Fake_Kraks"
        )

    elif message.text == "📞 Поддержка":
        await message.answer(
            "📩 Поддержка: @No_Fake_Kraks"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
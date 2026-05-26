import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

TOKEN = 8956006401:AAEUArB7IsF-ceqJoaTyOajUC_XMdLJ3s2M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💎 Купить MAGIC",
                url="https://t.me/No_Fake_Kraks"
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 Тарифы",
                callback_data="prices"
            ),
            InlineKeyboardButton(
                text="⭐ Отзывы",
                callback_data="reviews"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📖 Инструкция",
                callback_data="guide"
            ),
            InlineKeyboardButton(
                text="📞 Поддержка",
                url="https://t.me/No_Fake_Kraks"
            ),
        ],
    ]
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Добро пожаловать в Kraks Store\n\n"
        "💎 MAGIC для OXIDE\n"
        "💰 Цена: 280₽ / 1 день\n\n"
        "📞 покупка: @No_Fake_Kraks",
        reply_markup=main_keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
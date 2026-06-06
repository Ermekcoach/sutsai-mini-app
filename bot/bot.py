import os, asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('BOT_TOKEN')
WEBAPP_URL=os.getenv('WEBAPP_URL','https://your-domain.com')
BRAND_NAME=os.getenv('BRAND_NAME','Ермек Исламович')
if not TOKEN: raise RuntimeError('Укажите BOT_TOKEN в .env')
bot=Bot(TOKEN, parse_mode='HTML'); dp=Dispatcher()
@dp.message(CommandStart())
async def start(message:Message):
    kb=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔮 Открыть Сюцай-разбор', web_app=WebAppInfo(url=WEBAPP_URL))]])
    await message.answer(f'Здравствуйте! Это приложение цифрового разбора {BRAND_NAME}. Нажмите кнопку ниже, введите дату рождения и получите разбор.', reply_markup=kb)
async def main(): await dp.start_polling(bot)
if __name__=='__main__': asyncio.run(main())

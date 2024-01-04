import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6526588006:AAGgiJji0jmCtBpMBxqTGY335vrLN5lDHpM"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def answer_as_echo(message: types.Message):
    if message.text:
        await message.answer(text=message.text)
    elif message.sticker:
        await message.answer("sticker was used")
        await message.reply_sticker(sticker=message.sticker.file_id)

@dp.message()
async def reply_as_echo(message: types.Message):
    await message.reply(text=message.text)
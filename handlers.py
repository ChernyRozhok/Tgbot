from aiogram.types import Message

from main import bot, dp
from config import chat_id

async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler()
async def send_answer(message: Message):
    text = message.text
    await message.answer(text=text)
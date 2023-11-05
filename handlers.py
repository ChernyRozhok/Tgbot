from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard

from main import bot, dp
from config import chat_id

from anecdotes import anecdote1



@dp.message_handler(Command('start'))
async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Здравствуй',
                           reply_markup=keyboard)

@dp.message_handler()
async def send_anecdote(message: Message):
    await message.answer(f'{anecdote1}')




from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from aiogram import Bot

from keyboards import keyboard
from keyboards import keyboard1

from main import bot, dp
from config import chat_id

from anecdotes import anecdote1



@dp.message_handler(Command('start'))
async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Здравствуй',
                           reply_markup=keyboard1)

@dp.callback_query_handler()
async def send_anecdote(call: CallbackQuery):
    await call.message.answer(f'{anecdote1}')
    await call.answer()




# @dp.message_handler()
# async def send_anecdote(message: Message):
#     await message.answer(f'{anecdote1}')




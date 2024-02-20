from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from aiogram import Bot, types

from keyboards import keyboard1, keyboard2

from main import bot, dp
from config import chat_id

from api_requests import return_joke



@dp.message_handler(Command('start'))
async def send_hello(dp):
    await dp.answer(text='Здравствуй',
                    reply_markup=keyboard1)

@dp.callback_query_handler(text='greeting')
async def main_menu(call: CallbackQuery):
    await call.message.answer(f'Здравствуй',
                              reply_markup=keyboard1)
    await call.answer()


@dp.callback_query_handler(text='another_anecdote')
async def send_anecdote(call: CallbackQuery):
    await call.message.answer(f'{return_joke()}',
                              reply_markup=keyboard2)
    await call.answer()

@dp.callback_query_handler(text='anecdote')
async def send_anecdote(call: types.CallbackQuery):
    await call.message.edit_text(text=f'{return_joke()}',
                                 reply_markup=keyboard2)






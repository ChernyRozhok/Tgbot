from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from anecdotes import anecdote1

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Анекдот')
        ]
    ],
    resize_keyboard=True
)

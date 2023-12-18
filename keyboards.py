from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from anecdotes import anecdote1

keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Анекдот",
            callback_data="anecdote"
        )
    ],
])

keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Главное меню',
            callback_data='greeting'
        )
    ],
    [
        InlineKeyboardButton(
            text='Еще анекдот',
            callback_data='andecdote'
        )
    ]
])

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.types import FlatDetail


class FlatPaginatorCallbackData(CallbackData, prefix="flat"):
    page: int


def flat_paginator(max_page: int, page: int = 0) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️",
                    callback_data=FlatPaginatorCallbackData(
                        page=(page - 1) if page > 0 else max_page
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="➡️",
                    callback_data=FlatPaginatorCallbackData(
                        page=(page + 1) if page < max_page else 0
                    ).pack()
                )
            ]
        ]
    )
    return markup

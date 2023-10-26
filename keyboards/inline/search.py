from typing import Optional, Literal

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pydantic import PositiveInt, Field


class SearchCallbackData(CallbackData, prefix="search"):
    rooms: Optional[PositiveInt] = Field(default=None)
    price_from: Optional[PositiveInt] = Field(default=None)
    price_to: Optional[PositiveInt] = Field(default=None)
    city: Optional[str] = Field(default=None)
    region: Optional[str] = Field(default=None)
    action: Optional[Literal["next", "back"]] = Field(default=None)


rooms_count_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="1",
                callback_data=SearchCallbackData(
                    rooms=1
                ).pack()
            ),
            InlineKeyboardButton(
                text="2",
                callback_data=SearchCallbackData(
                    rooms=2
                ).pack()
            ),
            InlineKeyboardButton(
                text="3",
                callback_data=SearchCallbackData(
                    rooms=3
                ).pack()
            ),
            InlineKeyboardButton(
                text="4",
                callback_data=SearchCallbackData(
                    rooms=4
                ).pack()
            ),
            InlineKeyboardButton(
                text="5",
                callback_data=SearchCallbackData(
                    rooms=5
                ).pack()
            ),
            InlineKeyboardButton(
                text="6",
                callback_data=SearchCallbackData(
                    rooms=6
                ).pack()
            ),
        ],
        [
            InlineKeyboardButton(
                text="НАЗАД",
                callback_data=SearchCallbackData(
                    action="back"
                ).pack()
            ),
            InlineKeyboardButton(
                text="ДАЛЕЕ",
                callback_data=SearchCallbackData(
                    action="next"
                ).pack()
            )
        ]
    ]
)


city_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="МИНСК",
                callback_data=SearchCallbackData(
                    city="4cb07174-7b00-11eb-8943-0cc47adabd66"
                ).pack()
            ),
            InlineKeyboardButton(
                text="МОГИЛЕВ",
                callback_data=SearchCallbackData(
                    city="4cb0e950-7b00-11eb-8943-0cc47adabd66",
                    region="mogilev-region"
                ).pack()
            ),
            InlineKeyboardButton(
                text="БРЕСТ",
                callback_data=SearchCallbackData(
                    city="4c8f8db2-7b00-11eb-8943-0cc47adabd66",
                    region="brest-region"
                ).pack()
            ),
            InlineKeyboardButton(
                text="ГОМЕЛЬ",
                callback_data=SearchCallbackData(
                    city="4c95d414-7b00-11eb-8943-0cc47adabd66"
                ).pack()
            ),
            InlineKeyboardButton(
                text="ВИТЕБСК",
                callback_data=SearchCallbackData(
                    city="4c9236d8-7b00-11eb-8943-0cc47adabd66"
                ).pack()
            ),
            InlineKeyboardButton(
                text="ГРОДНО",
                callback_data=SearchCallbackData(
                    city="4c97eac6-7b00-11eb-8943-0cc47adabd66"
                ).pack()
            ),
        ]
    ]
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton(
                text="🔍 НАЙТИ"
            )
        ]
    ]
)

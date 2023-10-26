from aiogram.fsm.state import StatesGroup, State


class SearchStatesGroup(StatesGroup):
    rooms = State()
    price_from = State()
    price_to = State()
    city = State()
    search = State()

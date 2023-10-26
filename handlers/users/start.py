from json import dumps

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, URLInputFile, CallbackQuery

from keyboards.reply import main_keyboard_rkb
from utils.parsers import RealtParser
from states.search import SearchStatesGroup
from keyboards.inline import flat_paginator, FlatPaginatorCallbackData, rooms_count_ikb, SearchCallbackData, city_ikb


router = Router()


@router.message(F.text == "/start")
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Hello",
        reply_markup=main_keyboard_rkb
    )


@router.message(F.text == "🔍 НАЙТИ")
async def parse_command(message: Message, state: FSMContext):
    await state.clear()
    await message.delete()
    await state.set_state(state=SearchStatesGroup.rooms)
    await message.answer(
        text="Выбери количество комнат",
        reply_markup=rooms_count_ikb
    )


@router.callback_query(SearchStatesGroup.rooms, SearchCallbackData.filter(F.action == "back"))
async def get_rooms_count(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="Hello"
    )


@router.callback_query(SearchStatesGroup.rooms, SearchCallbackData.filter(F.action == "next"))
async def get_rooms_count(callback: CallbackQuery, state: FSMContext):
    await state.set_state(SearchStatesGroup.price_from)
    await callback.message.edit_text(
        text="Введи минимальную цену"
    )


@router.callback_query(SearchStatesGroup.rooms)
async def get_rooms_count(callback: CallbackQuery, state: FSMContext):
    callback_data = SearchCallbackData.unpack(callback.data)
    await state.set_state(SearchStatesGroup.price_from)
    await state.update_data(rooms=callback_data.rooms)
    await callback.message.edit_text(
        text="Введи минимальную цену"
    )


@router.message(SearchStatesGroup.price_from)
async def get_price_from(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.set_state(SearchStatesGroup.price_to)
        await state.update_data(priceFrom=message.text)
        await message.answer(
            text="Введи максимальную цену"
        )
    else:
        await message.answer(
            text="Неверное значение!"
        )


@router.message(SearchStatesGroup.price_to)
async def get_price_from(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.set_state(SearchStatesGroup.city)
        await state.update_data(priceTo=message.text)
        await message.answer(
            text="Выберите город",
            reply_markup=city_ikb
        )
    else:
        await message.answer(
            text="Неверное значение!"
        )


@router.callback_query(SearchStatesGroup.city)
async def get_city(callback: CallbackQuery, state: FSMContext):
    callback_data = SearchCallbackData.unpack(callback.data)
    state_data = await state.get_data()
    address = dumps([
        {"townUuid": callback_data.city}
    ])
    print(state_data)
    data = await RealtParser.get(
        params={
            "addressV2": address,
            "page": 1,
            "priceType": 840,
            **state_data
        },
        region=callback_data.region
    )
    await state.set_state(SearchStatesGroup.search)
    await state.update_data(flats=data)
    await callback.message.answer_photo(
        photo=URLInputFile(
            url=data[0].images[0].unicode_string()
        ),
        caption=data[0].caption,
        reply_markup=flat_paginator(max_page=len(data) - 1)
    )


@router.callback_query(FlatPaginatorCallbackData.filter())
async def paginator(callback: CallbackQuery, callback_data: FlatPaginatorCallbackData, state: FSMContext):
    data = await state.get_data()
    data = data.get("flats")
    flat = data[callback_data.page]
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=URLInputFile(
            url=flat.images[0].unicode_string() if flat.images else "https://media.moddb.com/images/articles/1/73/72743/image_error_full.png"
        ),
        caption=flat.caption,
        reply_markup=flat_paginator(max_page=len(data) - 1, page=callback_data.page)
    )

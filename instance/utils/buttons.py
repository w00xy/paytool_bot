from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from instance.kbds.inline import *
from instance.utils.extra import split_number, emoji_number


async def get_start_btns():
    return get_callback_btns(
        btns={
            "🛍 Товары": "products",
            "👏 О нас": "about",
        },
        sizes=(2,)

    )


home_btns = get_callback_btns(
        btns={
            "🏠 Главное меню": "start",
        },
        sizes=(2,)

    )


async def get_products_btns(products: list[list]):
    keyboard = InlineKeyboardBuilder()  # One button per row
    for product in products:
        product_id = product[0]
        product_name = product[1]
        button = InlineKeyboardButton(
            text=f"{product_name}",
            callback_data=f"product_{product_id}"
        )
        keyboard.add(button)  # Add button to the keyboard

    sizes = split_number(len(products))

    keyboard.add(InlineKeyboardButton(text=f"🏠 Главное меню", callback_data="start"))

    return keyboard.adjust(*sizes).as_markup()


async def get_product_btns(selected_id):
    keyboard = InlineKeyboardBuilder()
    for i in range(1, 7):
        keyboard.add(InlineKeyboardButton(text=f"🛒{emoji_number(i)}", callback_data=f"cart_add_{selected_id + 1}_{i}"))
    keyboard.add(InlineKeyboardButton(text=f"🏠Главное меню", callback_data="start"))

    return keyboard.adjust(3, 3, 1).as_markup()

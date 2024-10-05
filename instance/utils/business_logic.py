from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from instance.database.orm_query import orm_create_user, orm_get_products, add_item_to_cart
from instance.utils.buttons import *
from instance.utils.text import *


async def get_start_message(message: Message, session: AsyncSession):
    try:
        await orm_create_user(session, message.from_user.id, message.from_user.first_name)
    except:
        pass

    await message.answer(
        text=await get_start_text(message),
        reply_markup=await get_start_btns(),
    )


async def get_start_call(call: CallbackQuery):
    await call.message.edit_text(
        text=await get_start_text(call),
        reply_markup=await get_start_btns(),
    )


async def get_about_call(call: CallbackQuery):
    await call.message.edit_text(
        text=about_text,
        reply_markup=home_btns,
    )


async def get_products_message(call: CallbackQuery, session: AsyncSession, state: FSMContext):

    products = await orm_get_products(session)
    print(products)

    await call.message.edit_text(
        text=await get_products_text(),
        reply_markup=await get_products_btns(products),
    )


async def buy_product_message(call: CallbackQuery, session: AsyncSession, state: FSMContext):
    products = await orm_get_products(session)

    selected_id = int(call.data.split("_")[1]) - 1

    await call.message.edit_text(
        text=await get_product_text(products, selected_id),
        reply_markup=await get_product_btns(selected_id),
        parse_mode=ParseMode.MARKDOWN
    )


async def add_cart_message(call: CallbackQuery, session: AsyncSession, state: FSMContext):
    product_id = int(call.data.split("_")[-2])
    amount_add = int(call.data.split("_")[-1])

    await add_item_to_cart(session, user_id=call.from_user.id, product_id=product_id, quantity=amount_add)





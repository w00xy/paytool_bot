from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from instance.utils.business_logic import get_products_message, buy_product_message, add_cart_message
from instance.utils.states import BuyProduct

products_router = Router()


@products_router.callback_query(F.data == "products")
async def products_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()

    await get_products_message(call, session, state)


@products_router.callback_query(F.data.startswith("product_"))
async def but_product_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.set_state(BuyProduct.set_amount)

    await buy_product_message(call, session, state)


@products_router.callback_query(F.data.startswith("cart_add"))
async def cart_add_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.set_state(BuyProduct.set_amount)

    await add_cart_message(call, session, state)

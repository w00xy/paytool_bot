from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from instance.utils.business_logic import get_start_message, get_start_call, get_about_call

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    await get_start_message(message, session)


@start_router.callback_query(F.data == "start")
async def start_call_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()

    await get_start_call(call)


@start_router.callback_query(F.data == "about")
async def about_call_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()

    await get_about_call(call)

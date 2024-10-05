from aiogram.fsm.state import StatesGroup, State


class BuyProduct(StatesGroup):
    set_amount = State()

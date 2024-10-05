from aiogram.types import Message, CallbackQuery
from typing_extensions import Union


async def get_start_text(message: Union[Message, CallbackQuery]) -> str:
    return (
        f"*👋 Добро пожаловать в бот, {message.from_user.first_name}*\n\n"
        f"💸 Оплатить товары можно Криптовалютой или c Карты\n\n"
    )


about_text = (
    f"⭐️ Бот предоставляет доступ к покупке цифровых товаров\n\n"
)


async def get_products_text() -> str:
    return (
        f"*📒 Список всех товаров*\n\n"
        f"Выберите интересующую вас позицию: "
    )


async def get_product_text(products: list[list], product_id: int) -> str:
    print(product_id)
    product_name = products[product_id][1]
    product_price = products[product_id][2]
    product_desc = products[product_id][3]

    print(product_desc)

    return (
        f"*🔹 {product_name}*\n"
        f"*_________________*\n"
        f"{product_desc}\n\n"
        f"*Цена за ед* - *{product_price}*руб\n"
        f"💬 Используйте кнопки для выбора желаемого количества или напишите сколько вы хотите добавить в корзину: "
    )

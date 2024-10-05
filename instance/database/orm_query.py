from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from instance.database.models import User, Product, Cart, CartItem


async def orm_create_user(session: AsyncSession, user_id: id, user_first_name: str) -> None:
    """Создает пользователя в БД"""
    new_user = User(
        user_id=user_id,
        user_first_name=user_first_name,
    )
    session.add(new_user)

    await session.commit()


async def orm_get_products(session: AsyncSession) -> list[list]:
    """Получает список товаров из БД в виде списка списков."""
    query = select(Product)
    results = await session.execute(query)
    products = results.scalars().all()
    return [[product.id, product.name, product.price, product.description] for product in products]

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from instance.database.models import Product


async def orm_test_products(session: AsyncSession) -> None:

    selecting = select(Product.name).where(
        Product.name == "Apple Tokens RU"
    )
    result = await session.execute(selecting)
    if result.scalar() is not None:
        return

    new_product1 = Product(
        name="Apple Tokens RU",
        price=40,
        description="Подарочные карты Apple для аккаунта региона Россия\nВалюта подарочных карт рубли"
    )
    session.add(new_product1)

    new_product2 = Product(
        name="Apple Tokens USA",
        price=25,
        description="Подарочные карты Apple для аккаунта региона США\nВалюта подарочных карт доллары"
    )
    session.add(new_product2)

    await session.commit()

from sqlalchemy import String, DateTime, func, BigInteger, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    user_first_name: Mapped[str] = mapped_column((String(40)), nullable=True)
    money_paid: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    cart: Mapped["Cart"] = relationship("Cart", back_populates="user", uselist=False)


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column((String(40)), nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=True, default=10)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Cart(Base):
    __tablename__ = 'carts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship("User", back_populates="cart")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    total_price: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    items: Mapped["CartItem"] = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(Base):
    __tablename__ = 'cart_items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    product: Mapped["Product"] = relationship("Product", backref="cart_items")
    cart: Mapped["Cart"] = relationship("Cart", back_populates="items")

    @property
    def item_total_price(self):
        return self.quantity * self.product.price

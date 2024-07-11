from models.base import BaseType, Base

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey


class Order(Base):
    __tablename__ = 'Order'
    id: Mapped[BaseType.int_primary_key]
    order_time: Mapped[BaseType.update_time]
    status: Mapped[BaseType.str_100]  # <-- 做enum
    total_price: Mapped[float]

    user_id: Mapped[int] = mapped_column(ForeignKey('User.id', ondelete='cascade'))
    user: Mapped['User'] = relationship('User', back_populates='orders')

    order_items: Mapped[list["OrderItem"]] = relationship('OrderItem',
                                                          back_populates='order',
                                                          cascade="all, delete, delete-orphan",
                                                          lazy="select",
                                                          order_by="Order.id")

    def __init__(self, status: str, total_price: float, user_id: int):
        self.status = status
        self.total_price = total_price
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"<Order(id={self.id}, user_id=\"{self.user_id}\")> "


class OrderItem(Base):
    __tablename__ = 'OrderItem'
    id: Mapped[BaseType.int_primary_key]
    quantity: Mapped[int]
    sub_total: Mapped[float]

    order_id: Mapped[int] = mapped_column(ForeignKey("Order.id", ondelete='cascade'))
    order: Mapped["Order"] = relationship("Order", back_populates="order_items")

    store_item_id: Mapped[int] = mapped_column(ForeignKey("StoreItem.id", ondelete='cascade'))
    store_item: Mapped["StoreItem"] = relationship('StoreItem', back_populates="order_items")

    def __init__(self, quantity: int, sub_total: float, order_id: int, store_item_id: int):
        self.quantity = quantity
        self.sub_total = sub_total
        self.order_id = order_id
        self.store_id = store_item_id

    def __repr__(self) -> str:
        return f"<OrderItem(id={self.id}, order_id=\"{self.order_id}\")> "

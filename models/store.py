from models.base import BaseType, Base

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey


class Store(Base):
    __tablename__ = 'Store'
    id: Mapped[BaseType.int_primary_key]
    name: Mapped[BaseType.str_100]
    description: Mapped[BaseType.option_text]
    phone: Mapped[BaseType.option_str_100]
    address: Mapped[BaseType.option_text]

    items: Mapped[list["StoreItem"]] = relationship("StoreItem",
                                                    back_populates="store",
                                                    cascade="all, delete, delete-orphan",
                                                    lazy="select",
                                                    order_by="StoreItem.id")

    def __init__(self, name: str, description: str, phone: str, address: str):
        self.name = name
        self.description = description
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Store(id={self.id}, name=\"{self.name}\")> "


class StoreItem(Base):
    __tablename__ = 'StoreItem'
    id: Mapped[BaseType.int_primary_key]
    name: Mapped[BaseType.str_100]
    description: Mapped[BaseType.option_text]
    category: Mapped[BaseType.str_100]
    price: Mapped[float]
    is_active: Mapped[BaseType.bool_true]

    store_id: Mapped[int] = mapped_column(ForeignKey("Store.id", ondelete='cascade'))
    store: Mapped["Store"] = relationship("Store", back_populates="items")

    order_items: Mapped[list["OrderItem"]] = relationship("OrderItem",
                                                          back_populates="store_item",
                                                          cascade='all, delete, delete-orphan',
                                                          lazy="select",
                                                          order_by="OrderItem.id")

    def __init__(self, name: str, description: str, category: str, price: float, store_id: int, is_active: bool):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.store_id = store_id
        self.is_active = is_active

    def __repr__(self) -> str:
        return f"<StoreItem(id={self.id}, name={self.name}, is_active={self.is_active})> "



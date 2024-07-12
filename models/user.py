from typing import Optional

from models.base import BaseType, Base
from sqlalchemy.orm import relationship, Mapped


class User(Base):
    __tablename__ = 'User'

    id: Mapped[BaseType.int_primary_key]
    name: Mapped[BaseType.str_100]
    account: Mapped[BaseType.str_100]
    password: Mapped[BaseType.str_100]  # <-- 需要做加密
    phone: Mapped[BaseType.option_str_100]
    address: Mapped[BaseType.option_text]
    is_active: Mapped[BaseType.bool_true]

    orders: Mapped[list["Order"]] = relationship("Order",
                                                 back_populates="user",
                                                 cascade="all, delete, delete-orphan",
                                                 lazy="select",
                                                 order_by="Order.id")

    def __init__(self, name: str, account: str, password: str,
                 phone: Optional[str], address: Optional[str], id: int = None, is_active: bool = True) -> None:
        self.id = id
        self.name = name
        self.account = account
        self.password = password
        self.phone = phone
        self.address = address
        self.is_active = is_active

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"account=\"{self.account}\", " \
               f"name=\"{self.name}\", " \
               f"is_active={self.is_active})>"
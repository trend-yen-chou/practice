from contextlib import AbstractContextManager
from typing import Callable, Iterator, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.order import Order, OrderItem


class OrderRepo:

    def __init__(self, session_factory: Callable[...,  AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all_orders(self) -> Iterator[Order]:
        with self.session_factory() as session:
            return session.query(Order).all()

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        with self.session_factory() as session:
            order = session.query(Order).filter_by(id=order_id).first()
            if order is None:
                return None
            return order

    def get_order_items_by_order_id(self, order_id: int) -> Iterator[OrderItem]:
        with self.session_factory() as session:
            order_items = session.query(OrderItem).filter_by(OrderItem.order_id==order_id).all()
            return order_items

    def create_order(self, order: Order) -> Order:
        with self.session_factory() as session:
            session.add(order)
            session.commit()
            session.refresh(order)
            return order

    def create_order_item(self, order_item: OrderItem) -> OrderItem:
        with self.session_factory() as session:
            session.add(order_item)
            session.commit()
            session.refresh(order_item)
            return order_item

    def update_order(self, order_id: int, order: Order) -> Order:
        with self.session_factory() as session:
            entity = session.query(Order).filter_by(Order.id == order_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="Order not found")
            order.id = order_id
            session.merge(order)
            session.commit()
            return order

    def delete_order(self, order_id: int) -> None:
        with self.session_factory() as session:
            entity = session.query(Order).filter_by(Order.id==order_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="Order not found")
            session.delete(entity)
            session.commit()

    def delete_order_item(self, order_item_id: int) -> None:
        with self.session_factory() as session:
            entity = session.query(OrderItem).filter(OrderItem.id == order_item_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="Order not found")
            session.delete(entity)
            session.commit()



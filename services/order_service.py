from typing import Iterator

from models.order import Order, OrderItem
from repositories.order_repo import OrderRepo


class OrderService:

    def __init__(self, repository: OrderRepo):
        self._repository = repository

    def get_all_orders(self) ->  Iterator[Order]:
        return self._repository.get_all_orders()

    def get_order_by_id(self, order_id: int) -> Order:
        return self._repository.get_order_by_id(order_id)

    def get_order_item_by_id(self, order_id: int) -> Iterator[OrderItem]:
        return self._repository.get_order_items_by_order_id(order_id)

    def create_order(self, order: Order) -> Order:
        return self._repository.create_order(order)

    def create_order_item(self, order_item: OrderItem) -> OrderItem:
        return self._repository.create_order_item(order_item)

    def update_order(self, order_id: int, order: Order) -> Order:
        return self._repository.update_order(order_id, order)

    def delete_order(self, order_id: int) -> None:
        return self._repository.delete_order(order_id)

    def delete_order_item(self, order_item_id: int) -> None:
        return self._repository.delete_order_item(order_item_id)

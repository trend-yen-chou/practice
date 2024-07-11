from typing import Iterator

from repositories.store_repo import StoreRepo
from models.store import Store, StoreItem


class StoreService:

    def __init__(self, repository: StoreRepo):
        self._repository = repository

    def get_stores(self) -> Iterator[Store]:
        return self._repository.get_all_stores()

    def get_store_by_id(self, store_id: int) -> Store:
        return self._repository.get_store_by_id(store_id)

    def get_store_items_by_store_id(self, store_id: int) -> Iterator[StoreItem]:
        return self._repository.get_store_items_by_store_id(store_id)

    def create_store(self, store: Store) -> Store:
        return self._repository.create_store(store)

    def create_store_item(self, item: StoreItem) -> StoreItem:
        return self._repository.create_store_item(item)

    def update_store(self, store_id: int, store: Store) -> Store:
        return self._repository.update_store(store_id, store)

    def delete_store(self, store_id: int) -> None:
        self._repository.delete_store(store_id)

    def delete_store_item(self, item_id: int) -> None:
        self._repository.delete_store_item(item_id)

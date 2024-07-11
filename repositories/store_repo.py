from contextlib import AbstractContextManager
from typing import Callable, Iterator, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.store import Store, StoreItem


class StoreRepo:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all_stores(self) -> Iterator[Store]:
        with self.session_factory() as session:
            return session.query(Store).all()

    def get_store_by_id(self, store_id: int) -> Store:
        with self.session_factory() as session:
            store = session.query(Store).filter_by(Store.id==store_id).first()
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            return store

    def get_store_items_by_store_id(self, store_id: int) -> Iterator[StoreItem]:
        with self.session_factory() as session:
            store_items = session.query(StoreItem).filter(StoreItem.store_id==store_id).all()
            return store_items

    def create_store(self, store: Store) -> Store:
        with self.session_factory() as session:
            session.add(store)
            session.commit()
            session.refresh(store)
            return store

    def create_store_item(self, item: StoreItem) -> StoreItem:
        with self.session_factory() as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    def update_store(self,store_id: int, store: Store) -> Store:
        with self.session_factory() as session:
            entity = session.query(Store).filter_by(Store.id==store_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="User not found")
            store.id = entity.id
            session.merge(entity)
            session.commit()
            return entity

    def delete_store(self, store_id: int) -> None:
        with self.session_factory() as session:
            entity = session.query(Store).filter_by(Store.id==store_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="User not found")
            session.delete(entity)
            session.commit()

    def delete_store_item(self, item_id: int) -> None:
        with self.session_factory() as session:
            entity = session.query(StoreItem).filter(StoreItem.store_id==item_id).first()
            if not entity:
                raise HTTPException(status_code=404, detail="User not found")
            session.delete(entity)
            session.commit()





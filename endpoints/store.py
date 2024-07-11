from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from starlette import status

from schemas.store import StoreCreate, StoreItemCreate
from services.store_service import StoreService
from webapp.containers import Container
from models.store import Store, StoreItem

router = APIRouter(tags=["store"], prefix="/store")


@router.get("")
@inject
def get_stores(store_service: StoreService = Depends(Provide[Container.store_service])):
    return store_service.get_stores()


@router.get("/{store_id}")
@inject
def get_store_by_id(store_id: int,
                    store_service: StoreService = Depends(Provide[Container.store_service])):
    return store_service.get_store_by_id(store_id)


@router.get("/{store_id}/items")
@inject
def get_store_item_by_store_id(store_id: int,
                               store_service: StoreService = Depends(Provide[Container.store_service])):
    return store_service.get_store_items_by_store_id(store_id)


@router.post("/create_store", status_code=status.HTTP_201_CREATED)
@inject
def create_store(new_store: StoreCreate,
                 store_service: StoreService = Depends(Provide[Container.store_service])):
    new_store = Store(**new_store.model_dump())
    return store_service.create_store(new_store)


@router.post("/create_store_item", status_code=status.HTTP_201_CREATED)
@inject
def create_store_item(new_store_item: StoreItemCreate,
                      store_service: StoreService = Depends(Provide[Container.store_service])):
    new_store_item = StoreItem(**new_store_item.model_dump())
    return store_service.create_store_item(new_store_item)


@router.put("/update/{store_id}")
@inject
def update_store_by_id(store_id: int,
                       update_store: StoreItemCreate,
                       store_service: StoreService = Depends(Provide[Container.store_service])):
    update_store = Store(**update_store.model_dump())
    return store_service.update_store(store_id, update_store)


@router.delete("/{store_id}")
@inject
def delete_store(store_id: int,
                 store_service: StoreService = Depends(Provide[Container.store_service])):
    return store_service.delete_store(store_id)


@router.delete("/{store_item_id}")
@inject
def delete_store_item(store_id: int,
                      store_service: StoreService = Depends(Provide[Container.store_service])):
    return store_service.delete_store_item(store_id)
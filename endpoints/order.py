from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from starlette import status

from services.order_service import OrderService
from schemas.order import OrderCreate as OrderCreateSchema, OrderItemCreate as OrderItemCreateSchema
from models.order import Order, OrderItem

from webapp.containers import Container

router = APIRouter(tags=["order"], prefix="/order")


@router.get("")
@inject
def get_orders(order_service: OrderService = Depends(Provide[Container.order_service])):
    return order_service.get_all_orders()


@router.get("/{order_id}")
@inject
def get_order_by_id(order_id: int,
                    order_service: OrderService = Depends(Provide[Container.order_service])):
    return order_service.get_order_by_id(order_id)


@router.get("/{order_id}/items")
@inject
def get_order_items(order_id: int,
                    order_service: OrderService = Depends(Provide[Container.order_service])):
    return order_service.get_order_item_by_id(order_id)


@router.post("/create_order", status_code=status.HTTP_201_CREATED)
@inject
def create_order(
        new_order: OrderCreateSchema,
        order_service: OrderService = Depends(Provide[Container.order_service])):
    new_order = Order(**new_order.model_dump())
    return order_service.create_order(new_order)


@router.post("/create_order_iten", status_code=status.HTTP_201_CREATED)
@inject
def create_order_item(
        new_order_item: OrderItemCreateSchema,
        order_service: OrderService = Depends(Provide[Container.order_service])):
    new_order_item = OrderItem(**new_order_item.model_dump())
    return order_service.create_order_item(new_order_item)


@router.put("/update_order/{order_id}")
@inject
def update_order_by_id(order_id: int,
                       update_order: OrderCreateSchema,
                       order_service: OrderService = Depends(Provide[Container.order_service])):
    update_order = Order(**update_order.model_dump())
    return order_service.update_order(order_id, update_order)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_order(order_id: int,
                 order_service: OrderService = Depends(Provide[Container.order_service])):
    return order_service.delete_order(order_id)


@router.delete("/{order_item_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_order_item(order_item_id: int,
                      order_service: OrderService = Depends(Provide[Container.order_service])):
    return order_service.delete_order_item(order_item_id)

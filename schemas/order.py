from typing import Optional
from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    status: str = Field(max_length=100)
    total_price: float = Field()
    user_id: int = Field()


class OrderItemCreate(BaseModel):
    quantity: int = Field()
    sub_total: float = Field()
    order_id: int = Field()
    store_item_id: int = Field()
from typing import Optional

from pydantic import BaseModel, Field


class StoreCreate(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = Field()
    phone: Optional[str] = Field(max_length=100)
    address: Optional[str] = Field()


class StoreItemCreate(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = Field()
    category: Optional[str] = Field(max_length=100)
    price: float = Field()
    is_active: bool = Field(default=True)
    store_id: int = Field()



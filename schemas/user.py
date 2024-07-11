from typing import Optional

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=100)
    account: str = Field(max_length=100)
    password: str = Field(max_length=100)
    phone: Optional[str] = Field(max_length=100)
    address: Optional[str] = Field()


class UserUpdate(BaseModel):
    name: Optional[str] = Field(max_length=100)
    account: Optional[str] = Field(max_length=100)
    password: Optional[str] = Field(max_length=100)
    phone: Optional[str] = Field(max_length=100)
    address: Optional[str] = Field()
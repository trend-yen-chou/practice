from typing import Annotated, Optional
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Integer, DateTime, Text, Boolean


class Base(DeclarativeBase):
    pass


class BaseType(DeclarativeBase):
    int_primary_key = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    str_100 = Annotated[str, mapped_column(String(100))]
    option_str_100 = Annotated[Optional[str], mapped_column(String(100), nullable=True)]
    text = Annotated[str, mapped_column(Text)]
    option_text = Annotated[Optional[str], mapped_column(Text, nullable=True)]
    bool_true = Annotated[bool, mapped_column(Boolean, default=True)]
    update_time = Annotated[datetime, mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)]
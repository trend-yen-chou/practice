from contextlib import AbstractContextManager
from typing import Callable, Iterator, Optional
from sqlalchemy.orm import Session

from models.user import User


class UserRepo:

    def __init__(self, session_factory: Callable[...,  AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: int) -> Optional[User]:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            return user

    def create(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def update(self, user_id: int, user: User) -> Optional[User]:
        with self.session_factory() as session:
            entity: Optional[User, None] = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundException("User not found")
            user.id = entity.id
            session.merge(user)
            session.commit()
            return user

    def delete(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundException("User not found")
            session.delete(entity)
            session.commit()


class UserNotFoundException(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)

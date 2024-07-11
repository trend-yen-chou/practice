from typing import Iterator

from repositories.user_repo import UserRepo
from models.user import User


class UserService:

    def __init__(self, repository: UserRepo) -> None:
        self._repository: UserRepo = repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, user: User) -> User:
        return self._repository.create(user)

    def update_user(self, user_id: int, user: User) -> User:
        return self._repository.update(user_id, user)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete(user_id)

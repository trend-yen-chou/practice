from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
from starlette import status

from models.user import User
from services.user_service import UserService
from repositories.user_repo import UserNotFoundException
from webapp.containers import Container
from schemas.user import UserCreate as UserCreateSchema
from schemas.user import UserUpdate as UserUpdateSchema

router = APIRouter(tags=["user"], prefix="/user")


@router.get("")
@inject
def get_all(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_users()


@router.get("/{user_id}")
@inject
def get_by_id(user_id: int,
              user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_user_by_id(user_id)


@router.post("", status_code=status.HTTP_201_CREATED)
@inject
def create(new_user: UserCreateSchema,
           user_service: UserService = Depends(Provide[Container.user_service])):
    entity = User(
        name=new_user.name,
        account=new_user.account,
        password=new_user.password,
        phone=new_user.phone,
        address=new_user.address,
    )
    return user_service.create_user(entity)


@router.put("/update/{user_id}")
@inject
def update(
        user_id: int,
        update_user: UserUpdateSchema,  # 格式轉換的時機
        user_service: UserService = Depends(Provide[Container.user_service])):
    try:
        user_entity = User(
            name=update_user.name,
            account=update_user.account,
            password=update_user.password,
            phone=update_user.phone,
            address=update_user.address)
        return user_service.update_user(user_id, user_entity)
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_by_id(user_id: int,
                 user_service: UserService = Depends(Provide[Container.user_service])):
    try:
        user_service.delete_user_by_id(user_id)
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)




import json
from unittest import mock
import pytest
from fastapi.testclient import TestClient

from repositories.user_repo import UserRepo, UserNotFoundException
from models.user import User
from webapp.application import app


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_users(client):
    repository_mock = mock.Mock(spec=UserRepo)
    repository_mock.get_all.return_value = [
        User(id=1, name="test1", account="test1@email.com", password="pwd", phone="123456", address="tw",
             is_active=True),
        User(id=2, name="test2", account="test2@email.com", password="pwd", phone="123456", address="jp",
             is_active=False),
    ]

    with app.container.user_repository.override(repository_mock):
        response = client.get("/user")

    assert response.status_code == 200
    data = response.json()
    assert data == [
        {"id": 1, "name": "test1", "account": "test1@email.com",
         "password": "pwd", "phone": "123456", "address": "tw", "is_active": True},
        {"id": 2, "name": "test2", "account": "test2@email.com",
         "password": "pwd", "phone": "123456", "address": "jp", "is_active": False},
    ]


def test_get_user_by_id(client):
    repository_mock = mock.Mock(spec=UserRepo)
    repository_mock.get_by_id.return_value = User(id=1,
                                                  name="test1",
                                                  account="test1@email.com",
                                                  password="pwd",
                                                  phone='123456',
                                                  address='tw',
                                                  is_active=True)
    with app.container.user_repository.override(repository_mock):
        response = client.get("/user/1")

    assert response.status_code == 200
    data = response.json()
    assert data == {"id": 1, "name": "test1", "account": "test1@email.com",
                    "password": "pwd", "phone": "123456", "address": "tw", "is_active": True}


def test_user_create(client):
    repository_mock = mock.Mock(spec=UserRepo)
    repository_mock.create.return_value = User(
        id=1,
        name="test1",
        account="email",
        password="pwd",
        phone='123456',
        address='tw',
        is_active=True
    )

    test_case = {
        "name": "test1",
        "account": "email",
        "password": "pwd",
        "phone": "123456",
        "address": "tw"
    }

    with app.container.user_repository.override(repository_mock):
        response = client.post("/user", json=test_case)

    assert response.status_code == 201
    data = response.json()
    assert data == {"id": 1, "name": "test1", "account": "email",
                    "password": "pwd", "phone": "123456", "address": "tw", "is_active": True}


def test_user_remove(client):
    repository_mock = mock.Mock(spec=UserRepo)
    with app.container.user_repository.override(repository_mock):
        response = client.delete("/user/1")
    assert response.status_code == 204


def test_user_remove_404(client):
    repository_mock = mock.Mock(spec=UserRepo)
    repository_mock.delete.side_effect = UserNotFoundException("User not found")

    with app.container.user_repository.override(repository_mock):
        response = client.delete("/users/1")

    assert response.status_code == 404

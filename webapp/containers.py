from dependency_injector import containers, providers

from webapp.database import Database

from repositories.user_repo import UserRepo
from repositories.store_repo import StoreRepo
from repositories.order_repo import OrderRepo
from services.user_service import UserService
from services.store_service import StoreService
from services.order_service import OrderService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["endpoints.user", "endpoints.store", "endpoints.order"])
    config = providers.Configuration(yaml_files=['config.yml'])

    db = providers.Singleton(
        Database,
        db_url=config.DB.URL)

    # Repository
    user_repository = providers.Factory(
        UserRepo,
        session_factory=db.provided.session
    )

    store_repository = providers.Factory(
        StoreRepo,
        session_factory=db.provided.session
    )

    order_repository = providers.Factory(
        OrderRepo,
        session_factory=db.provided.session
    )

    # Service
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )

    store_service = providers.Factory(
        StoreService,
        repository=store_repository
    )

    order_service = providers.Factory(
        OrderService,
        repository=order_repository
    )



from fastapi import FastAPI

from webapp.containers import Container
from endpoints.user import router as user_router
from endpoints.store import router as store_router
from endpoints.order import router as order_router

def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container

    app.include_router(user_router)
    app.include_router(store_router)
    app.include_router(order_router)

    return app


app = create_app()

import logging
from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.store import Store, StoreItem
from models.order import Order, OrderItem

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        print(db_url)
        self._engine = create_engine(db_url, echo=True, pool_pre_ping=True)
        self._session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            )
        )

    def create_database(self) -> None:
        Base.metadata.create_all(
            bind=self._engine,
            tables=[User.__table__,
                    Order.__table__,
                    OrderItem.__table__,
                    Store.__table__,
                    StoreItem.__table__],)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because og exception")
            session.rollback()
            raise
        finally:
            session.close()

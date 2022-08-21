from typing import Any

import sqlalchemy.orm

from src.model import db_connectors as conn
from src.model import models as models


class Session:
    def __init__(self):
        self.session = self.get_session()

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()

    def get_by_id(self, model, id) -> Any:
        return self.session.query(model).get(id)

    @staticmethod
    def get_session() -> sqlalchemy.orm.sessionmaker:
        connector = conn.ConnectorSqlite()
        session = connector.get_session()
        create_all()
        return session


# is in its own function because it has to be called every time when opening a session and not only when importing
def create_all():
    models.Base.metadata.create_all(conn.ConnectorSqlite().get_engine())

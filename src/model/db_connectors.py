import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(autocommit=False, autoflush=False)


class ConnectorSqlite:
    connection_string = 'sqlite:///test.db'

    def __init__(self):
        self.engine = create_engine(self.connection_string)
        Session.configure(bind=self.engine)

    @staticmethod
    def get_session() -> sqlalchemy.orm.sessionmaker:
        return Session()

    def get_engine(self) -> sqlalchemy.engine.base.Engine:
        return self.engine

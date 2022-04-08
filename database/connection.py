from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLITE_PATH = 'flutes.db'


def get_engine():
    return create_engine(
        f'sqlite:///{SQLITE_PATH}'
    )


def get_session() -> Session:
    return sessionmaker(bind=get_engine())()

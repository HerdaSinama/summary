from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

sync_engine = create_engine(
    config.sync_database_url,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
)

sync_local_session = sessionmaker(bind=sync_engine)

@contextmanager
def get_sync_session():
    session = sync_local_session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
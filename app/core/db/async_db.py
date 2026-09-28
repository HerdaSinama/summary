from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import config

async_engine = create_async_engine(config.DATABASE_URL)

async_local_session = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_async_session():
    async with async_local_session() as session:
        yield session
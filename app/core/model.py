from uuid import UUID, uuid4
from typing import Self

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True, default=lambda: uuid4())


    async def save(
        self,
        async_session: AsyncSession,
    ) -> Self:
        async_session.add(self)
        await async_session.commit()

        return self

    @classmethod
    async def get(
        cls,
        id: UUID,
        async_session: AsyncSession,
    ):
        ...

    async def delete(self, async_session: AsyncSession):
        await async_session.delete(self)
        await async_session.commit()
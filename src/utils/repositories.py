from abc import ABC, abstractmethod

from sqlalchemy import select, insert, update
from sqlalchemy.exc import SQLAlchemyError

from databases.payments import async_session_maker
from src.models.users import Users


class AbstractRepository(ABC):
    @abstractmethod
    async def insert_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def select_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, **kwargs):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def insert_one(self, **kwargs):
        async with async_session_maker() as session:
            try:
                stmt = insert(self.model).values(**kwargs).returning(self.model)
                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one_or_none()
            except SQLAlchemyError as e:
                return {'An error occurred': str(e)}

    async def select_one(self, identifier: int):
        async with async_session_maker() as session:
            try:
                stmt = select(self.model).filter(self.model.id == identifier)
                result = await session.execute(stmt)
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}

    async def update_one(self, **kwargs):
        async with async_session_maker() as session:
            try:
                if 'id' not in kwargs:
                    raise ValueError('Missing "id" in arguments')

                stmt = (
                    update(self.model)
                    .values(**kwargs)
                    .where(self.model.id == kwargs['id'])
                    .returning(self.model)
                )

                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}

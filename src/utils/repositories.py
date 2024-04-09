from abc import ABC, abstractmethod

from sqlalchemy import select, insert, update

from databases.payments import async_session_maker


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
                return {'status': result.scalar_one_or_none()}
            except Exception as e:
                return {'An error occurred': e}

    async def select_one(self, **kwargs):
        async with async_session_maker() as session:
            try:
                stmt = select(self.model).filter_by(**kwargs)
                result = await session.execute(stmt)
                return {'status': result.scalar_one_or_none()}
            except Exception as e:
                return {'An error occurred': e}

    async def update_one(self, **kwargs):
        async with async_session_maker() as session:
            try:
                stmt = update(self.model).values(**kwargs).returning(self.model)
                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}

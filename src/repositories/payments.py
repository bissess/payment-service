from sqlalchemy import select, update

from databases.payments import async_session_maker
from models.users import User
from utils.repositories import SQLAlchemyRepository


class PaymentRepository(SQLAlchemyRepository):
    model = User

    async def insert_one(self, user_id: int):
        async with async_session_maker() as session:
            try:
                user = select(self.model.balance).where(self.model.id == user_id)
                result = await session.execute(user)
                await session.commit()
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}

    async def select_one(self, user_id: int):
        async with async_session_maker() as session:
            try:
                balance = select(self.model.balance).where(self.model.id == user_id)
                result = await session.execute(balance)
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}

    async def update_one(self, user_id: int, new_balance: float):
        async with async_session_maker() as session:
            try:
                stmt = update(self.model).where(self.model.id == user_id).values(balance=new_balance)
                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one_or_none()
            except Exception as e:
                return {'An error occurred': e}



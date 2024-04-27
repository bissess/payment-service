import pytest
import pytest_asyncio

from src.schemas.users import PaymentSchema
from src.databases.payments import engine, Base, async_session_maker
from src.utils.config import settings
from src.models.users import Users


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_payments():

    payments = [
        Users(id=1, username='b1ssee', balance=100, currency='dollar'),
        Users(id=2, username='user', balance=200, currency='dollar'),
        Users(id=3, username='guest', balance=300, currency='dollar'),
        Users(id=4, username='anonym', balance=400, currency='dollar'),
        Users(id=5, username='qwerty', balance=500, currency='dollar'),
        Users(id=6, username='user777', balance=500, currency='dollar'),
        Users(id=7, username='python7', balance=500, currency='dollar'),
        Users(id=8, username='guest123', balance=500, currency='dollar'),
        Users(id=9, username='noname', balance=500, currency='dollar'),
        Users(id=10, username='developer', balance=500, currency='dollar'),
    ]

    async with async_session_maker() as session:
        for payment in payments:
            session.add(payment)
        await session.commit()




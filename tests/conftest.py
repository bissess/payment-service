import pytest_asyncio

from src.databases.payments import engine, Base
from src.utils.config import settings
from src.models.users import Users


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

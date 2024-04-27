import pytest
import pytest_asyncio

from src.models.users import Users
from src.utils.repositories import SQLAlchemyRepository


class TestSQLAlchemyRepository(SQLAlchemyRepository):
    model = Users

    @pytest_asyncio.fixture(autouse=True)
    async def setup_repository(self):
        self.repository = TestSQLAlchemyRepository()

    # @pytest.mark.asyncio
    # async def test_insert_one(self, payments):
    #
    #     for payment in payments:
    #         result = await self.repository.insert_one(**payment.model_dump())
    #         assert result is not None, 'Result should not be None'
    #         print(f'INSERTED RESULTS: {result}')

    @pytest.mark.asyncio
    async def test_select_one(self):
        user_id = 1
        result = await self.repository.select_one(identifier=user_id)
        assert result is not None
        print(f'SELECTED RESULT: {result.__dict__}')

    @pytest.mark.asyncio
    async def test_update_one(self):
        user_id = 1
        amount = 20000

        user = await self.repository.select_one(identifier=user_id)
        assert user is not None, f'User with ID: {user_id} does not exist'

        balance = user.balance
        new_balance = balance + amount

        updated_balance = await self.repository.update_one(id=user_id, balance=new_balance)
        assert updated_balance is not None, f'Failed to update balance for {user_id}'





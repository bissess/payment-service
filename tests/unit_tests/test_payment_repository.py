import pytest
import pytest_asyncio

from repositories.payments import PaymentRepository
from schemas.users import PaymentSchema


class TestPaymentRepository(PaymentRepository):

    @pytest_asyncio.fixture(autouse=True)
    async def setup_repository(self):
        self.repository = PaymentRepository()

    @pytest.mark.asyncio
    @pytest.mark.parametrize('data', [
        ({'id': 1, 'username': 'b1ssee', 'balance': 100, 'currency': 'dollar'})
    ])
    async def test_insert_one(self, data):
        result = await self.repository.insert_one(data)
        assert result is not None

    @pytest.mark.asyncio
    @pytest.mark.parametrize('user_balance, expected_balance', [
        (1, 100)
    ])
    async def test_select_one(self, user_balance, expected_balance):
        user = await self.repository.select_one(user_balance)
        assert user == expected_balance
        print(f'User balance: {user} equal to expected balance: {expected_balance}')

    @pytest.mark.asyncio
    @pytest.mark.parametrize('identifier, new_balance', [
        (1, 400)
    ])
    async def test_update_one(self, identifier, new_balance):
        user_before = await self.repository.select_one(user_id=identifier)
        balance_before = user_before

        await self.repository.update_one(identifier, new_balance)

        user_after = await self.repository.select_one(user_id=identifier)
        balance_after = user_after

        assert balance_after == new_balance

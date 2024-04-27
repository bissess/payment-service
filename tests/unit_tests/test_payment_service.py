import pytest

from repositories.payments import PaymentRepository
from services.payments import PaymentService


@pytest.fixture
def service():
    return PaymentService(PaymentRepository)


class TestPaymentService:
    # @pytest.mark.asyncio
    # async def test_inserting_data(self, service, payments):
    #     for payment in payments:
    #         result = await service.repository.insert_one(**payment.model_dump())
    #         assert result is not None, 'Данные не были записаны в БД'

    @pytest.mark.asyncio
    async def test_replenishment_balance(self, service):
        identifier = 1
        assert identifier is not None, 'User not found'
        amount = 100
        result = await service.replenishment_balance(identifier, amount)

        user = await service.repository.select_one(identifier=identifier)
        assert user.balance == 200, 'Value of balance not equal to 300'

    @pytest.mark.asyncio
    async def test_withdraw_balance(self, service):
        identifier = 2
        assert identifier is not None, f'User with ID: ({identifier}) does not exist'
        amount = 200

        result = await service.withdraw_balance(identifier, amount)

        user = await service.repository.select_one(identifier=identifier)
        assert user.balance == 0, 'Balance of user not equal to 0'

    @pytest.mark.asyncio
    async def test_transfer_balance(self, service):
        sender_id = 3
        receiver_id = 1
        amount = 300
        assert sender_id is not None or receiver_id is not None, 'User not found'

        result = await service.transfer_balance(sender_id, receiver_id, amount)

    @pytest.mark.asyncio
    async def test_getting_balance(self, service):
        identifier = 1
        assert identifier is not None, f'User with ID: ({identifier}) not found'
        result = await service.getting_balance(identifier)

        user = await service.repository.select_one(identifier=identifier)
        assert user is not None, 'User does not exist'

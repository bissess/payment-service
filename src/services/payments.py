from fastapi import HTTPException

from repositories.payments import PaymentRepository


class PaymentService:
    def __init__(self, repository):
        self.repository: PaymentRepository = repository()

    async def replenishment_balance(self, identifier: int, amount: float):
        if identifier is None:
            raise HTTPException(status_code=404, detail='User not found')
        user = await self.repository.select_one(identifier=identifier)

        if amount <= 0:
            raise HTTPException(status_code=400, detail='Value must be greater than 0 for replenishment')
        replenishment = user.balance + amount

        result = await self.repository.update_one(id=identifier, balance=replenishment)

    async def withdraw_balance(self, identifier: int, amount: float):
        if identifier is None:
            raise HTTPException(status_code=404, detail='User not found')
        user = await self.repository.select_one(identifier=identifier)

        if user.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance for withdraw")
        withdraw = user.balance - amount

        result = await self.repository.update_one(id=identifier, balance=withdraw)

    async def transfer_balance(self, sender_id: int, receiver_id: int, amount: float):
        if sender_id is None or receiver_id is None:
            raise HTTPException(status_code=404, detail='User not found')
        sender = await self.repository.select_one(identifier=sender_id)
        receiver = await self.repository.select_one(identifier=receiver_id)

        if sender.balance < amount:
            raise HTTPException(status_code=400, detail='Insufficient balance for transfer')
        sender_balance = sender.balance - amount
        receiver_balance = receiver.balance + amount

        sender_result = await self.repository.update_one(id=sender_id, balance=sender_balance)
        receiver_result = await self.repository.update_one(id=receiver_id, balance=receiver_balance)

    async def getting_balance(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail='User not found')

        current_balance = await self.repository.select_one(identifier=identifier)
        return current_balance

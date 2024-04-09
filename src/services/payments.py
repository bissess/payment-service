from repositories.payments import PaymentRepository


class PaymentService:
    def __init__(self, repository):
        self.repository: PaymentRepository = repository()

    async def recharge_balance(self, user_id: int, amount: float):
        if amount <= 0:
            return {'message': 'Value must be greater than 0'}

        user_balance = await self.repository.select_one(user_id)
        recharge_balance = user_balance + amount
        await self.repository.update_one(user_id, recharge_balance)

        return recharge_balance

    async def withdraw_balance(self, user_id: int, amount: float):
        user_balance = await self.repository.select_one(user_id)
        withdraw_balance = user_balance - amount
        await self.repository.update_one(user_id, withdraw_balance)

        return withdraw_balance

    async def transfer_balance(self, sender_id: int, receiver_id: int, amount: float):
        sender_balance = await self.repository.select_one(sender_id)
        receiver_balance = await self.repository.select_one(receiver_id)

        if sender_balance < amount:
            return {'message': 'Недостаточно средств.'}

        sender_balance -= amount
        receiver_balance += amount

        await self.repository.update_one(sender_id, sender_balance)
        await self.repository.update_one(receiver_id, receiver_balance)

        return {'message': 'Transfer has been successfully'}

    async def get_balance(self, user_id: int):
        return await self.repository.select_one(user_id)

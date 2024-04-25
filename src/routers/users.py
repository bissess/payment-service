from fastapi import APIRouter, Depends

from dependencies.payments import get_payment_service
from services.payments import PaymentService

router = APIRouter(
    prefix='/api/balance',
    tags=['Balance']
)


@router.post('/replenishment/')
async def replenishment_balance(identifier: int, amount: float, service: PaymentService = Depends(get_payment_service)):
    replenishment_result = await service.replenishment_balance(identifier, amount)
    return {'message': f'Replenishment for user with ID: ({identifier}) has been successfully completed.'}


@router.post('/withdraw/')
async def withdraw_balance(identifier: int, amount: float, service: PaymentService = Depends(get_payment_service)):
    withdraw_result = await service.withdraw_balance(identifier, amount)
    return {'message': f'Withdrawal from ID: ({identifier}) in the amount of ({amount}) has been successfully completed.'}


@router.post('/transfer/')
async def transfer_balance(
        sender_id: int,
        receiver_id: int,
        amount: float,
        service: PaymentService = Depends(get_payment_service)):
    transfer_result = await service.transfer_balance(sender_id, receiver_id, amount)
    return {'message': 'Transfer has been successfully.'}


@router.get('')
async def getting_balance(identifier: int, service: PaymentService = Depends(get_payment_service)):
    getting_result = await service.getting_balance(identifier)
    return getting_result

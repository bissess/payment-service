from fastapi import APIRouter, Depends, HTTPException

from dependencies.payments import get_payment_service
from services.payments import PaymentService

router = APIRouter(
    prefix='/api/balance',
    tags=['Balance']
)


@router.post('/deposit/')
async def recharge_deposit(user_id: int, amount: float, service: PaymentService = Depends(get_payment_service)):
    if user_id is None:
        raise HTTPException(status_code=404, detail='User not found')

    return await service.recharge_balance(user_id, amount)


@router.post('/withdraw/')
async def withdraw_balance(user_id: int, amount: float, service: PaymentService = Depends(get_payment_service)):
    if user_id is None:
        raise HTTPException(status_code=404, detail='User not found')

    return await service.withdraw_balance(user_id, amount)


@router.post('/transfer/')
async def transfer_balance(sender_id: int, receiver_id: int, amount: float,
                           service: PaymentService = Depends(get_payment_service)):
    return await service.transfer_balance(sender_id, receiver_id, amount)


@router.get('')
async def get_balance(user_id: int, service: PaymentService = Depends(get_payment_service)):
    if user_id is None:
        raise HTTPException(status_code=404, detail='User not found')

    return await service.get_balance(user_id)


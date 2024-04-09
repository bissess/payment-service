from repositories.payments import PaymentRepository
from services.payments import PaymentService


def get_payment_service() -> PaymentService:
    return PaymentService(PaymentRepository)
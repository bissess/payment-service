import pytest

from schemas.users import PaymentSchema


@pytest.fixture
def payments():
    payments = [
        PaymentSchema(id=1, username='b1ssee', balance=0, currency='dollar'),
        PaymentSchema(id=2, username='user', balance=0, currency='dollar'),
        PaymentSchema(id=3, username='guest', balance=0, currency='dollar'),
    ]
    return payments

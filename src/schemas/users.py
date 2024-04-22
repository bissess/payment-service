from pydantic import BaseModel


class PaymentSchema(BaseModel):
    id: int
    username: str
    balance: float
    currency: str

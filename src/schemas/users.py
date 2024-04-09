from pydantic import BaseModel


class RechargeDepositSchema(BaseModel):
    id: int
    username: str
    balance: float
    currency: str

from models.users import Users
from utils.repositories import SQLAlchemyRepository


class PaymentRepository(SQLAlchemyRepository):
    model = Users


from src.models.classModels import User, Transaction
from dataclasses import dataclass

@dataclass
class TransactionDao:
    transaction: Transaction

    def get_from(self) -> User:
        return self.transaction.From

    def get_to(self) -> User:
        return self.transaction.to

    def get_amount(self) -> float:
        return self.transaction.amount



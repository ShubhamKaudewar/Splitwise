from src.models.classModels import Expense, User, UserShareMap, UserList
from dataclasses import dataclass
from typing import List

@dataclass
class ExpenseDao:
    user: User
    expense: Expense

    def get_id(self) -> str:
        return self.expense.id

    def get_description(self) -> str:
        return self.expense.description

    def get_amount(self) -> float:
        return self.expense.amount

    def get_payer(self) -> User:
        return self.expense.payer

    def get_participants(self) -> UserList:
        return self.expense.participants

    def get_shares(self) -> UserShareMap:
        return self.expense.shares



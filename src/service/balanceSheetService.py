from src.models.classModels import User, Expense, BalanceSheet, Transaction
from src.service.expenseService import ExpenseObserver
from dataclasses import dataclass
from typing import List

@dataclass
class BalanceSheetService(ExpenseObserver):
    balances: BalanceSheet

    def on_expense_added(self, expense: Expense):
        pass

    def on_expense_updated(self, expense: Expense):
        pass

    def update_balances(self):
        pass

    def get_balance(self) -> float:
        pass

    def get_total_balance(self, user: User) -> float:
        pass

    def get_simplified_settlements(self) -> List[Transaction]:
        pass

    def get_sub_optimal_minimum_settlements(self) -> int:
        pass

    def get_optimal_minimum_settlements(self) -> int:
        pass

    def sum_of_mask(self) -> float:
        pass

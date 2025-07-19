from src.models.classModels import Expense, ExpenseObserver, ExpenseList
from abc import ABC, abstractmethod
from dataclasses import dataclass

class ExpenseObserver(ABC):
    @abstractmethod
    def on_expense_added(self, expense: Expense):
        pass

    @abstractmethod
    def on_expense_updated(self, expense: Expense):
        pass

@dataclass
class ExpenseManager:
    observer: ExpenseObserver
    expenses: Expense

    def add_observer(self) -> None:
        pass

    def remove_observer(self) -> None:
        pass

    def notify_expense_added(self) -> None:
        pass

    def notify_expense_updated(self) -> None:
        pass

    def add_expense(self) -> None:
        pass

    def update_expense(self) -> None:
        pass
    
    def get_all_expenses(self) -> ExpenseList:
        pass
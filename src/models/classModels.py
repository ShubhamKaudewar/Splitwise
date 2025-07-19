from pydantic import BaseModel
from typing import List, Dict, TypeAlias
from enum import StrEnum
from src.service.expenseService import ExpenseObserver

class SplitStrategy(StrEnum):
    EQUAL = "equally"
    UNEQUAL = "unequally"
    PERCENTAGE = "percentage"

class GroupType(StrEnum):
    FRIENDS = "friends"
    FAMILY = "family"
    UNI = "uni"
    OFFICE = "office"

class User(BaseModel):
    id: int
    name: str
    email: str


# Type aliases
UserList: TypeAlias = List[User]
UserShareMap: TypeAlias = Dict[User, float]


class Group(BaseModel):
    groupId: int
    name: str
    listOfUsers: UserList
    typeOfGroup: SplitStrategy


class Expense(BaseModel):
    id: str
    description: str
    amount: float
    payer: User
    participants: UserList
    shares: UserShareMap

ExpenseList: TypeAlias = List[Expense]

class Transaction(BaseModel):
    From: User
    to: User
    amount: float

class UserPair(BaseModel):
    user1: User
    user2: User

class BalanceSheet(BaseModel):
    balances: Dict[UserPair, float]

class ExpenseManager(BaseModel):
    observers: List[ExpenseObserver]
    expenses: List[Expense]
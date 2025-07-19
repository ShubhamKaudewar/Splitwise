from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import override

from src.models.classModels import UserShareMap, UserList, SplitStrategy

class Split(ABC):
    @abstractmethod
    def calculate_split(self, amount: float, participants: UserList, split_details: UserShareMap) -> UserShareMap:
        pass

    def create_split(self, strategy: str) -> UserShareMap:
        if strategy == SplitStrategy.EQUAL:
            return EqualSplit().calculate_split(
                amount=100,
                participants=[],
                split_details={}
            )
        elif strategy == SplitStrategy.PERCENTAGE:
            return PercentageSplit().calculate_split(
                amount=100,
                participants=[],
                split_details={}
            )
        else:
            raise Exception("strategy not implemented!")


@dataclass
class PercentageSplit(Split):
    @override
    def calculate_split(self, amount: float, participants: UserList, split_details: UserShareMap) -> UserShareMap:
        split: UserShareMap = {}

        per_head_amount = amount / len(participants)
        for user in split_details:
            split[user] = per_head_amount
        return split


@dataclass
class EqualSplit(Split):
    @override
    def calculate_split(self, amount: float, participants: UserList, split_details: UserShareMap) -> UserShareMap:
        split: UserShareMap = {}

        per_head_amount = amount / len(participants)
        for user in participants:
            split[user] = per_head_amount
        return split


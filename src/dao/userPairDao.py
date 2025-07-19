from src.models.classModels import User, UserPair
from dataclasses import dataclass

@dataclass
class UserPairDao:
    userPair: UserPair

    def get_user_1(self) -> User:
        return self.userPair.user1

    def get_user_2(self) -> User:
        return self.userPair.user2


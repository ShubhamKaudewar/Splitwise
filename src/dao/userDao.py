from src.models.classModels import User
from dataclasses import dataclass

@dataclass
class UserDao:
    user: User

    def get_id(self) -> int:
        return self.user.id

    def get_name(self) -> str:
        return self.user.name

    def get_email(self) -> str:
        return self.user.email

    def equals(self, obj) -> bool:
        if self.user == obj:
            return True
        if not isinstance(obj, User):
            return False
        if obj.id == self.get_id():
            return True
        return False





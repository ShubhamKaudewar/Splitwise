from src.dao import UserDao
from hashlib import md5
from base64 import urlsafe_b64encode
from dataclasses import dataclass
from src.models import User

# Logger
import logging
logger = logging.getLogger("USER SERVICE")

@dataclass
class UserService:
    user: User

    def add_expense(self, amount):
        pass

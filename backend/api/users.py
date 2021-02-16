from dataclasses import dataclass
from enum import Enum


@dataclass
class User:
    id: int
    firstName: str
    lastName: str
    login: str
    password: str

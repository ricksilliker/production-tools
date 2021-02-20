from dataclasses import dataclass


@dataclass
class User:
    id: int
    firstName: str
    lastName: str
    login: str
    password: str
    hardwareProfileID: int

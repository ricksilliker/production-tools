from dataclasses import dataclass
from enum import Enum


class OSType(Enum):
    windows = 'Windows'
    mac = 'MacOS'
    linux = 'Linux'


@dataclass
class Hardware:
    id: int
    operatingSystem: OSType
    distro: str
    version: str
    cpu: str
    gpu: list[str]
    ram: list[str]
    storage: list[str]
    accessories: list[str]
    installedSoftware: list[int]

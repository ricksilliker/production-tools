from dataclasses import dataclass


@dataclass
class Software:
    id: int
    displayName: str
    exeURI: str
    category: str

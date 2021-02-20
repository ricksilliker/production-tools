from dataclasses import dataclass
from enum import Enum




class ProjectType(Enum):
    commercial = 'Commercial'
    feature = 'Feature'
    game = 'Game'
    software = 'Software'
    web = 'Web'


@dataclass
class ProjectItem:
    id: int
    name: str
    code: str
    imageURI: str
    type: ProjectType
    internal: bool


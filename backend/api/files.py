from dataclasses import dataclass
from enum import Enum


class FileType(Enum):
    source = 'Source'
    image = 'Image'
    movie = 'Movie'
    cache = 'Cache'
    archive = 'Archive'
    pdf = 'PDF'
    delivery = 'Delivery'
    resource = 'Resource'
    incoming = 'Incoming'


@dataclass
class ProjectFile:
    id: int
    pathURI: str
    name: str
    type: FileType
    createdAt: str
    size: int

from dataclasses import dataclass
from enum import Enum


class VersionType(Enum):
    review = 'Review'
    Work = 'Work'
    Publish = 'Publish'
    Vendor = 'Vendor'


class ReviewStatus(Enum):
    standby = 'Standby'
    nextUp = 'Next Up'
    inReview = 'In Review'
    reviewed = 'Review Complete'


@dataclass
class VersionItem:
    id: int
    taskID: int
    fileID: int
    number: int
    descriptor: str
    type: VersionType
    previewURI: str
    reviewStatus: ReviewStatus

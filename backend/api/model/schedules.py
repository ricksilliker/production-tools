from dataclasses import dataclass
from enum import Enum


class PassStatus(Enum):
    app = 'Approved'
    apt = 'Approved With Tweak'
    itn = 'Internal'
    crv = 'Client Review'
    ph1 = 'Phase 1'
    ph2 = 'Phase 2'


class RatingCode(Enum):
    a = 'A'
    b = 'B'
    c = 'C'


@dataclass
class ScheduleEntryItem:
    id: int
    taskID: int
    bid: float
    estimatedEffort: float
    actualEffort: float
    currentPass: PassStatus
    rating: RatingCode


@dataclass
class ScheduleItem:
    id: int
    name: str
    entries: list[ScheduleEntryItem]

from dataclasses import dataclass
from enum import Enum


class DepartmentCode(Enum):
    art = 'Art'
    rigging = 'Rigging'
    lighting = 'Lighting'
    animation = 'Animation'


class StatusCode(Enum):
    ready = 'Ready To Start'
    inProgress = 'In Progress'
    complete = 'Complete'
    hold = 'Hold'
    blocked = 'Blocked'
    omit = 'Omit'


@dataclass
class TaskItem:
    id: int
    name: str
    department: DepartmentCode
    assigneeID: int
    reviewerID: int
    priority: int
    startDate: str
    dueDate: str
    startedAt: str
    completedAt: str
    linkID: int
    projectID: int
    status: StatusCode
    description: str

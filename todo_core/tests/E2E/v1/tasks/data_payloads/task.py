from dataclasses import dataclass


@dataclass()
class TaskPayload:
    name: str
    description: str


@dataclass()
class TaskData:
    id: str
    name: str
    description: str
    status: str | None
    deadline: str | None
    assigner_id: str | None
    project_id: str
    created_at: str | None

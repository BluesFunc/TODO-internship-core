from dataclasses import dataclass

from projects.choices import ProjectCollaboratorRole


@dataclass(slots=True)
class ProjectPayloadData:
    name: str
    description: str


@dataclass
class ProjectCollaboratorPayload:
    user_id: str
    role: ProjectCollaboratorRole

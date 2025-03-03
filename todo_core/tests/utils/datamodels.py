from dataclasses import dataclass
from uuid import UUID

from common.choices import ProjectPermissions, Roles, TaskPermissions
from projects.choices import ProjectCollaboratorRole


@dataclass(slots=True)
class MissingIdUserData:
    mail: str


@dataclass(slots=True)
class ProjectData:
    id: UUID
    name: str
    description: str
    creator_id: UUID


@dataclass
class UserTokenPayload:
    mail: str
    user_id: str
    role: list[Roles | None]
    permissions: list[ProjectPermissions | TaskPermissions | None]


@dataclass(slots=True)
class ProjectCollaboratorData:
    user_id: UUID
    project_id: UUID
    role: ProjectCollaboratorRole


@dataclass(slots=True)
class ProjectPayloadData:
    name: str
    description: str

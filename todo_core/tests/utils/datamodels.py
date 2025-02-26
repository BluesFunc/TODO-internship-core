from dataclasses import dataclass

from common.choices import ProjectPermissions, Roles
from projects.choices import ProjectCollaboratorRole


@dataclass(slots=True)
class MissingIdUserData:
    mail: str


@dataclass(slots=True)
class ProjectData:
    id: str
    name: str
    description: str
    creator_id: str


@dataclass
class UserDataPayload:
    mail: str
    user_id: str
    role: list[Roles | None]
    permissions: list[ProjectPermissions | None]


@dataclass(slots=True)
class ProjectCollaboratorData:
    user_id: str
    project_id: str
    role: ProjectCollaboratorRole

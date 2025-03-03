from dataclasses import dataclass
from uuid import UUID

from common.choices import ProjectPermissions, Roles, TaskPermissions


@dataclass
class UserData:
    mail: str
    user_id: UUID
    role: list[Roles]
    permissions: list[ProjectPermissions | TaskPermissions | None]

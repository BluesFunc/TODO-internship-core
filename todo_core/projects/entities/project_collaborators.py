from dataclasses import dataclass
from uuid import UUID

from projects.choices import ProjectCollaboratorRole
from projects.models import Project


@dataclass
class ProjectCollaboratorEntity:
    project_id: Project
    user_id: UUID
    role: ProjectCollaboratorRole

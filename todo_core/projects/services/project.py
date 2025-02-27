from uuid import UUID

from projects.models import Project


class ProjectService:

    @staticmethod
    def get_by_id(project_id: UUID) -> Project:
        return Project.objects.get(id=project_id)

    @staticmethod
    def is_creator(user_id: UUID, project: Project) -> bool:
        return project.creator_id == user_id

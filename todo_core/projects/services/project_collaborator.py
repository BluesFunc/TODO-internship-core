from uuid import UUID

from projects.models import Project, ProjectCollaborators


class ProjectCollaboratorsService:

    @staticmethod
    def create(collaborator: ProjectCollaborators) -> ProjectCollaborators:
        collaborator.save()
        return collaborator

    @staticmethod
    def is_collaborator(user_id: UUID, project: Project) -> bool:
        return ProjectCollaborators.objects.filter(
            user_id=user_id, project_id=project
        ).exists()

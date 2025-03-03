from uuid import UUID

from django.core.exceptions import ObjectDoesNotExist

from projects.choices import ProjectCollaboratorRole
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

    @staticmethod
    def is_project_editor(user_id: UUID, project: Project) -> bool:
        try:
            collaborator = ProjectCollaborators.objects.get(
                project_id=project, user_id=user_id
            )
        except ObjectDoesNotExist:
            return False
        return collaborator.role == ProjectCollaboratorRole.EDITOR.value

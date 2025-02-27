from uuid import UUID

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import ProjectCollaborators
from projects.services import ProjectCollaboratorsService, ProjectService


class IsProjectCollaboratorReaderPermission(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        try:
            project_id = view.kwargs.get("project_pk")
            project_id = UUID(project_id)
            project = ProjectService.get_by_id(project_id)
            user_id = request.user_data.user_id
        except ValueError as ve:
            raise ValidationError(ve)
        return ProjectCollaboratorsService.is_collaborator(user_id, project)

    def has_object_permission(
        self, request: Request, view: APIView, obj: ProjectCollaborators
    ) -> bool:
        return self.has_permission(request, view)

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.services import ProjectCollaboratorsService, ProjectService


class IsHaveTaskAccess(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        user_id = request.user_data.user_id
        project_id = view.kwargs.get("project_pk")
        project = ProjectService.get_by_id(project_id)
        if project is None:
            return False
        return ProjectCollaboratorsService.is_collaborator(user_id, project)

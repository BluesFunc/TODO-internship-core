from uuid import UUID

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.services import ProjectService


class IsProjectCollaboratorEditorPermission(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:

        user_id = request.user_data.user_id
        project_id = UUID(view.kwargs.get("project_pk"))
        project = ProjectService.get_by_id(project_id)
        return ProjectService.is_creator(user_id, project)

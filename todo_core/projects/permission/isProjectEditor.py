from uuid import UUID

from projects.models import ProjectCollaborators
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class IsProjectEditorPermission(BasePermission):
    message = "User is not project editor"

    def has_permission(self, request: Request, view: GenericViewSet) -> bool:

        try:
            project_id = UUID(view.kwargs.get("project_pk"))
            user_id = UUID(request.user_data["user_id"])
            collaborator = ProjectCollaborators.objects.get(
                user_id=user_id, project_id=project_id
            )
        except Exception:
            return False
        return collaborator.role == "E"

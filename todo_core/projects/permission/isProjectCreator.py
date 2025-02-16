from uuid import UUID

from projects.models import Project
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class IsProjectCreatorPermission(BasePermission):
    message = "User is not creator"

    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        try:
            project_id = view.kwargs.get("project_pk")
            if not project_id:
                project_id = view.kwargs.get("pk")
            project_id = UUID(project_id)
            user_id = UUID(request.user_data["user_id"])
        except Exception:
            return False
        return Project.objects.filter(id=project_id, creator_id=user_id).exists()

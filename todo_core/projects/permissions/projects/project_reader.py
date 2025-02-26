from uuid import UUID

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import ProjectCollaborators


class IsProjectViewerPermission(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        try:
            project_id = view.kwargs.get("pk")
            project_id = UUID(project_id)
            user_id = request.user_data.user_id
        except ValueError as ve:
            raise ValidationError(ve)
        return ProjectCollaborators.objects.filter(
            user_id=user_id, project_id=project_id
        ).exists()

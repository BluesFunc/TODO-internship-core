from uuid import UUID

from projects.models import Project
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsProjectCollaboratorEditorPermission(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        try:
            project_id = view.kwargs.get("project_pk")
            project_id = UUID(project_id)
            user_id = request.user_data["user_id"]
        except ValueError as ve:
            raise ValidationError(ve)
        return Project.objects.filter(id=project_id, creator_id=user_id).exists()

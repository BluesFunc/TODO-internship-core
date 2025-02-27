from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import ProjectCollaborators
from projects.services import ProjectService


class IsProjectCollaboratorEditorPermission(BasePermission):

    def has_object_permission(
        self, request: Request, view: APIView, obj: ProjectCollaborators
    ) -> bool:

        user_id = request.user_data.user_id
        project = obj.project_id
        return ProjectService.is_creator(user_id, project)

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from common.choices import ProjectPermissions
from projects.models import Project
from projects.services import ProjectCollaboratorsService


class IsReadProjects(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        return ProjectPermissions.get.value in request.user_data.permissions

    def has_object_permission(
        self, request: Request, view: APIView, obj: Project
    ) -> bool:
        user_id = request.user_data.user_id
        return ProjectCollaboratorsService.is_collaborator(user_id, obj)

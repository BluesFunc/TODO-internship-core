from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from common.choices import TaskPermissions
from projects.services import ProjectCollaboratorsService
from tasks.models import Task


class IsGetTaskPermission(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return TaskPermissions.create.value in request.user_data.permissions

    def has_object_permission(self, request: Request, view: APIView, obj: Task) -> bool:
        user_id = request.user_data.user_id
        project = obj.project_id
        return ProjectCollaboratorsService.is_collaborator(user_id, project)

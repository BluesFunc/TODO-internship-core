from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from common.choices import TaskPermissions
from projects.services import ProjectCollaboratorsService, ProjectService


class IsCreateAndEditTasksPermission(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        user_id = request.user_data.user_id
        project_id = view.kwargs.get("project_pk")
        project = ProjectService.get_by_id(project_id)
        if project is None:
            return False
        is_editor = ProjectCollaboratorsService.is_project_editor(user_id, project)
        return (
            is_editor and TaskPermissions.create.value in request.user_data.permissions
        )

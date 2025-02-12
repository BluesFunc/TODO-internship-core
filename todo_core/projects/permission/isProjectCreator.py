from projects.models import Project
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class IsProjectCreatorPermission(BasePermission):

    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(id=project_id)
        user_id = request.user_data["user_id"]
        creator_id = str(project.creator_id)
        return creator_id == user_id

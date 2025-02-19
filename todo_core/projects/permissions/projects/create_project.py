from common.permissions import ProjectPermissions
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsCreateProjectPermission(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return ProjectPermissions.create.value in request.user_data["permissions"]

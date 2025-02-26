from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from common.choices import ProjectPermissions


class IsReadProjects(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        return ProjectPermissions.get.value in request.user_data.permissions

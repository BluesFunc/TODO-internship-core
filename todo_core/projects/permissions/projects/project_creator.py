from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import Project


class IsProjectCreatorPermission(BasePermission):

    def has_object_permission(
        self, request: Request, view: APIView, obj: Project
    ) -> bool:
        user_id = request.user_data.user_id
        return obj.creator_id == user_id

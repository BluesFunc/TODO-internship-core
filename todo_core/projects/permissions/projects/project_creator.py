from projects.models import Project
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsProjectCreatorPermission(BasePermission):

    def has_object_permission(
        self, request: Request, view: APIView, obj: Project
    ) -> bool:
        try:
            user_id = request.user_data["user_id"]
        except KeyError:
            return False
        return obj.creator_id == user_id

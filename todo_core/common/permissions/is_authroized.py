from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class IsJwtAuthorizedPermisson(BasePermission):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        return request.user_data

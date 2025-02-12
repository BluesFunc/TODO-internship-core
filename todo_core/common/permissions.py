from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class isJwtAuthorizedPermisson(BasePermission):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        return hasattr(request, "user_data") and request.user_data

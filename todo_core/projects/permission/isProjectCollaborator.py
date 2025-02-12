from uuid import UUID

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class isProjectCollaboratorPermission(BasePermission):

    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        user_id = UUID(request.user_data["user_id"])
        collaborators = view.queryset
        for collaborator in collaborators:
            if user_id == collaborator.user_id:
                return True
        return False

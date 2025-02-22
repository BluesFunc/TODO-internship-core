from typing import Protocol

from rest_framework.permissions import BasePermission


class PermissionActionViewSetProtocol(Protocol):
    permission_classes: list[BasePermission]

    def get_permissions(self) -> list[BasePermission]: ...

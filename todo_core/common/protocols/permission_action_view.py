from typing import Iterable, Protocol

from rest_framework.permissions import BasePermission


class PermissionActionViewSetProtocol(Protocol):
    permission_classes: Iterable[BasePermission]

    def get_permissions(self) -> Iterable[BasePermission]: ...

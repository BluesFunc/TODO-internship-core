from common.protocols import PermissionActionViewSetProtocol
from rest_framework.permissions import BasePermission


class ActionPermissionViewSetMixin(PermissionActionViewSetProtocol):
    """
    Mixin extend GenericViewSet.
    Provide action_classes_permission attribute.
    It is structured as:
    action_classes_permission = {
    'action_name' : [Permissions, ...]
    ....
    }
    Mixin allow to write dictionary, where permission are defined  for each action.
    """

    action_classes_permission: dict[str, list[BasePermission]]

    def get_permissions(self) -> list[BasePermission]:
        view_actions = self.action_classes_permission
        if self.action in view_actions:
            permissions = self.action_classes_permission[self.action]
            self.permission_classes.extend(permissions)
        return [permission() for permission in self.permission_classes]

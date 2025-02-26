from rest_framework.permissions import BasePermission

from common.protocols import PermissionActionViewSetProtocol


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
            action_permissions = self.permission_classes + permissions
        return [permission() for permission in action_permissions]

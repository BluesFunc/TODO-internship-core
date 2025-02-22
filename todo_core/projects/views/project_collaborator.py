from common.mixins import ActionPermissionViewSetMixin
from common.permissions import IsJwtAuthorizedPermisson
from projects.filters import ProjectCollaboratorFilterBackend
from projects.models import ProjectCollaborators
from projects.permissions import (
    IsProjectCollaboratorEditorPermission,
    IsProjectCollaboratorReaderPermission,
)
from projects.serializers import ProjectCollaboratorSerializer
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class ProjectCollaboratorViewSet(ActionPermissionViewSetMixin, viewsets.ModelViewSet):

    serializer_class = ProjectCollaboratorSerializer
    queryset = ProjectCollaborators.objects.all()
    filter_backends = [ProjectCollaboratorFilterBackend]
    permission_classes = [IsJwtAuthorizedPermisson]
    action_classes_permission = {
        "retrieve": [IsProjectCollaboratorReaderPermission],
        "create": [IsProjectCollaboratorEditorPermission],
        "list": [IsProjectCollaboratorReaderPermission],
        "destroy": [IsProjectCollaboratorEditorPermission],
        "update": [IsProjectCollaboratorEditorPermission],
        "partial_update": [IsProjectCollaboratorEditorPermission],
    }

    def create(self, request: Request, project_pk: str) -> Response:
        data = {**request.data, "project_id": project_pk}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

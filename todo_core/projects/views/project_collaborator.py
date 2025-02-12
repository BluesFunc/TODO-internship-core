from common.permissions import isJwtAuthorizedPermisson
from projects.filters import ProjectCollaboratorFilterBackend
from projects.models import ProjectCollaborators
from projects.permission import isProjectCollaboratorPermission
from projects.serializers import ProjectCollaboratorSerializer
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class ProjectCollaboratorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = ProjectCollaboratorSerializer
    queryset = ProjectCollaborators.objects.all()
    filter_backends = [ProjectCollaboratorFilterBackend]
    permission_classes = [isJwtAuthorizedPermisson, isProjectCollaboratorPermission]

    def create(self, request: Request) -> Response:
        project_id = self.kwargs.get("project_pk")
        data = {**request.data, "project_id": project_id}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

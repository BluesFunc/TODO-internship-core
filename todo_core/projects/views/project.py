from common import IsJwtAuthorizedPermisson
from django.db.models import QuerySet
from projects.models import Project, ProjectCollaborators
from projects.permission import (
    IsProjectCollaboratorPermission,
    IsProjectCreatorPermission,
)
from projects.serializers.project import ProjectSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsJwtAuthorizedPermisson]

    def get_queryset(self) -> QuerySet[Project]:
        user_id = self.request.user_data["user_id"]
        projects = Project.objects.filter(collaborators__user_id=user_id)
        return projects

    def get_permissions(self) -> list[BasePermission]:
        if self.action in ("retrive"):
            self.permission_classes.append(IsProjectCollaboratorPermission)
        elif self.action in ("update", "destroy"):
            self.permission_classes.append(IsProjectCreatorPermission)
        return super().get_permissions()

    def create(self, request: Request) -> Response:
        creator_id = request.user_data.get("user_id", "42")
        print(creator_id)
        serializer = self.get_serializer(
            data={**request.data, "creator_id": creator_id}
        )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer: BaseSerializer) -> Project:
        try:
            project = serializer.save()
            user_id = serializer.data.get("creator_id")
            collaborator = ProjectCollaborators.objects.create(
                user_id=user_id, project_id=project, role="E"
            )
            collaborator.save()
        except Exception as e:
            raise e
        return project

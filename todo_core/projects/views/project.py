from common import IsJwtAuthorizedPermisson
from common.mixins import ActionPermissionViewSetMixin
from django.db.models import QuerySet
from projects.choices import ProjectCollaboratorRole
from projects.entities import ProjectCollaboratorEntity
from projects.models import Project
from projects.permissions import (
    IsCreateProjectPermission,
    IsProjectCreatorPermission,
    IsProjectViewerPermission,
    IsReadProjects,
)
from projects.serializers import ProjectSerializer
from projects.services import ProjectCollaboratorsService
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class ProjectViewSet(ActionPermissionViewSetMixin, viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsJwtAuthorizedPermisson]
    action_classes_permission = {
        "retrieve": [IsReadProjects, IsProjectViewerPermission],
        "create": [IsCreateProjectPermission],
        "list": [IsReadProjects],
        "destroy": [IsProjectCreatorPermission],
        "update": [IsProjectCreatorPermission],
        "partial_update": [IsProjectCreatorPermission],
    }

    def get_queryset(self) -> QuerySet[Project]:
        user_id = self.request.user_data["user_id"]
        projects = Project.objects.filter(collaborators__user_id=user_id)
        return projects

    def create(self, request: Request) -> Response:
        creator_id = request.user_data.get("user_id")
        serializer = self.get_serializer(
            data={**request.data, "creator_id": creator_id}
        )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer: ProjectSerializer) -> Project:
        project = serializer.save()
        collaborator_data = {
            "project_id": project,
            "user_id": serializer.data.get("creator_id"),
            "role": ProjectCollaboratorRole.EDITOR,
        }
        collaborator = ProjectCollaboratorEntity(**collaborator_data)
        ProjectCollaboratorsService.create(collaborator)
        return project

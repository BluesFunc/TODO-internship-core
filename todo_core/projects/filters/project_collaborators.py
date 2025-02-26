from django.db.models.query import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet


class ProjectCollaboratorFilterBackend(BaseFilterBackend):
    def filter_queryset(
        self, request: Request, queryset: QuerySet, view: GenericViewSet
    ) -> QuerySet:
        project_id = view.kwargs.get("project_pk", "")
        return queryset.filter(project_id=project_id)

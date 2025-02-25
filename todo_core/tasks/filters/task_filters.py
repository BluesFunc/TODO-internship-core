from uuid import UUID

from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from tasks.models import Task


class TaskFilters(BaseFilterBackend):
    def filter_queryset(
        self, request: Request, queryset: QuerySet[Task], view: GenericAPIView
    ) -> QuerySet[Task]:
        project_id = UUID(view.kwargs.get("project_pk"))
        return queryset.filter(project_id=project_id)

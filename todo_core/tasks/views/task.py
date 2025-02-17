from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from tasks.filters import TaskFilters
from tasks.models import Task
from tasks.serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [TaskFilters]

    @action(detail=True, methods=["create"])
    def deadline(self, request: Request, pk: str) -> Response:
        pass

    @action(
        detail=True,
        methods=["create"],
    )
    def subscribe(self, request: Request) -> Response:
        pass

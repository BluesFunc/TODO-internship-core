from django.core.exceptions import BadRequest
from django.db import IntegrityError
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from tasks.filters import TaskFilters
from tasks.models import Task, TaskStatusSubscribers
from tasks.serializer import TaskSerializer
from tasks.services import TaskStatusSubscriberService


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [TaskFilters]

    @action(detail=True, methods=["patch"])
    def deadline(self, request: Request, pk: str) -> Response:
        pass

    @action(
        detail=True,
        methods=["create", "update"],
    )
    def subscribe(self, request: Request, pk: str) -> Response:
        user_id = request.user_data["user_id"]
        entity = TaskStatusSubscribers(user_id=user_id, task_id=pk)
        try:
            subscriber = TaskStatusSubscriberService.create(entity=entity)
        except IntegrityError as ie:
            raise BadRequest(ie)
        return Response(subscriber)

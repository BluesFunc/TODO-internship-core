from uuid import UUID

from django.core.exceptions import BadRequest, ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from common.mixins import MultiSerializerViewSetMixin
from tasks.filters import TaskFilters
from tasks.models import Task, TaskStatusSubscribers
from tasks.schemas import TaskDeadlineSchema
from tasks.serializer import TaskSerializer
from tasks.services import TaskService, TaskStatusSubscriberService


class TaskViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [TaskFilters]

    serializer_action_classes = {
        "deadline": TaskDeadlineSchema,
        "subscribe": BaseSerializer,
    }

    def create(self, request: Request, project_pk: str) -> Response:
        project_id = UUID(project_pk)
        data = {**request.data, "project_id": project_id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=True, methods=["patch"])
    def deadline(self, request: Request, project_pk: str, pk: str) -> Response:
        task = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deadline = serializer.data["deadline"]
        TaskService.set_deadline(task, deadline)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=["post"])
    def subscribe(self, request: Request, project_pk: str, pk: str) -> Response:
        user_id = request.user_data.user_id
        task = self.get_object()
        entity = TaskStatusSubscribers(user_id=user_id, task_id=task)
        try:
            TaskStatusSubscriberService.create(entity)
        except IntegrityError as ie:
            raise BadRequest(ie)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"])
    def unsubscribe(self, request: Request, project_pk: str, pk: str) -> Response:
        user_id = request.user_data.user_id
        task = self.get_object()
        try:
            TaskStatusSubscriberService.delete(task, user_id)
        except ObjectDoesNotExist as oe:
            raise BadRequest(oe)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

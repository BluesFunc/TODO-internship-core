from uuid import UUID

from django.core.exceptions import BadRequest, ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from common.mixins import ActionPermissionViewSetMixin, MultiSerializerViewSetMixin
from common.permissions import IsJwtAuthorizedPermission
from common.tools import MailSender
from tasks.models import Task, TaskStatusSubscribers
from tasks.permissions import (
    IsCreateAndEditTasksPermission,
    IsGetTaskPermission,
    IsHaveTaskAccess,
)
from tasks.schemas import TaskDeadlineSchema, TaskStatusSchema
from tasks.serializer import TaskSerializer
from tasks.services import TaskService, TaskStatusSubscriberService


class TaskViewSet(
    ActionPermissionViewSetMixin, MultiSerializerViewSetMixin, ModelViewSet
):
    serializer_class = TaskSerializer
    permission_classes = [IsJwtAuthorizedPermission, IsHaveTaskAccess]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]

    action_classes_permission = {
        "list": [IsGetTaskPermission],
        "retrieve": [IsGetTaskPermission],
        "create": [IsCreateAndEditTasksPermission],
        "update": [IsCreateAndEditTasksPermission],
        "partial_update": [IsCreateAndEditTasksPermission],
        "delete": [IsCreateAndEditTasksPermission],
        "deadline": [IsCreateAndEditTasksPermission],
    }

    serializer_action_classes = {
        "status": TaskStatusSchema,
        "deadline": TaskDeadlineSchema,
        "subscribe": BaseSerializer,
    }

    def get_queryset(self) -> QuerySet[Task]:
        project_id = UUID(self.kwargs.get("project_pk"))
        return Task.objects.filter(project_id=project_id)

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
    def status(self, request: Request, **kwargs: str) -> Response:
        try:
            task = self.get_object()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            task_status = serializer.data["status"]
            TaskService.set_status(task, task_status)
        except IntegrityError as ie:
            raise BadRequest(ie)
        headers = self.get_success_headers(serializer.data)
        user_mail = request.user_data.mail
        MailSender.send_change_task_status_notification(user_mail, task)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=["patch"])
    def deadline(self, request: Request, **kwargs: str) -> Response:
        try:
            task = self.get_object()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            deadline = serializer.data["deadline"]
            TaskService.set_deadline(task, deadline)
        except IntegrityError as ie:
            raise BadRequest(ie)
        headers = self.get_success_headers(serializer.data)
        user_mail = request.user_data.mail
        MailSender.send_subscribe_notification(user_mail, task)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=["post"])
    def subscribe(self, request: Request, **kwargs: str) -> Response:
        user_id = request.user_data.user_id
        task = self.get_object()
        entity = TaskStatusSubscribers(user_id=user_id, task_id=task)
        try:
            TaskStatusSubscriberService.create(entity)
        except IntegrityError as ie:
            raise BadRequest(ie)
        user_mail = request.user_data.mail
        MailSender.send_subscribe_notification(user_mail, task)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"])
    def unsubscribe(self, request: Request, **kwargs: str) -> Response:
        user_id = request.user_data.user_id
        task = self.get_object()
        try:
            TaskStatusSubscriberService.delete(task, user_id)
        except ObjectDoesNotExist as oe:
            raise BadRequest(oe)
        user_mail = request.user_data.mail
        MailSender.send_unsubscribe_message(user_mail, task)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

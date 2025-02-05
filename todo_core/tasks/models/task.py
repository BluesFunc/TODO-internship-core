import uuid

from common.models import TimeStampedModel
from django.db import models
from projects.models.project import Project

from ..choices.task_status import TaskStatus


class Task(TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, null=False)
    description = models.TextField()
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )
    status = models.CharField(max_length=2, choices=TaskStatus, default=TaskStatus.TODO)
    deadline = models.DateTimeField(default=None, null=True)
    assigner_id = models.UUIDField(default=None, null=True)

    class Meta:
        db_table = "task"

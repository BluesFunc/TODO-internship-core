import uuid

from django.db import models
from django.utils.translation import gettext_lazy
from projects.models import Project, TimeStampedModel


class Task(TimeStampedModel):

    class TaskStatus(models.TextChoices):
        TODO = "TD", gettext_lazy("To do")
        PROGRESS = "P", gettext_lazy("In progress")
        COMPLETE = "C", gettext_lazy("Complete")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=300, null=False)
    description = models.TextField()
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )
    status = models.CharField(max_length=2, choices=TaskStatus, default=TaskStatus.TODO)
    deadline = models.DateTimeField(default=None)
    assigner_id = models.UUIDField(default=None)

    class Meta:
        db_table = "task"


class TaskStatusSubscribers(TimeStampedModel):

    task_id = models.ForeignKey(
        "Task", primary_key=True, null=False, on_delete=models.CASCADE
    )
    user_id = models.UUIDField(null=False)

    class Meta:
        db_table = "task_status_subscribers"
        unique_together = (("task_id", "user_id"),)

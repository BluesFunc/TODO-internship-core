import uuid
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Task(TimeStampedModel):

    class TaskStatus(models.TextChoices):
        TODO = "TD", gettext_lazy("To do")
        PROGRESS = "P", gettext_lazy("In progress")
        COMPLETE = "C", gettext_lazy("Complete")

    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    name = models.CharField(max_length=300, null=False)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=TaskStatus, default=TaskStatus.TODO)
    deadline = models.DateTimeField(default=None)
    assigner_id = models.UUIDField(default=None)

    class Meta:
        db_table = "task"


class Task_Status_Subscribers(TimeStampedModel):

    task_id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField(primary_key=True)

    class Meta:
        db_table = "task_status_subscribers"

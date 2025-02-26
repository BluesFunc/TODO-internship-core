from uuid import uuid4

from django.db import models

from common.models import TimeStampedModel


class TaskStatusSubscribers(TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid4)
    task_id = models.ForeignKey("Task", null=False, on_delete=models.CASCADE)
    user_id = models.UUIDField(
        null=False,
    )

    class Meta:
        db_table = "task_status_subscribers"
        unique_together = (("task_id", "user_id"),)

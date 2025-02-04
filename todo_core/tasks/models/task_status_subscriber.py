from common.models import TimeStampedModel
from django.db import models


class TaskStatusSubscribers(TimeStampedModel):

    task_id = models.ForeignKey(
        "Task", primary_key=True, null=False, on_delete=models.CASCADE
    )
    user_id = models.UUIDField(
        null=False,
    )

    class Meta:
        db_table = "task_status_subscribers"
        unique_together = (("task_id", "user_id"),)

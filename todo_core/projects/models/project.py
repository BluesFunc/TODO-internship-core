import uuid

from common.models import TimeStampedModel
from django.db import models


class Project(TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, null=False)
    description = models.TextField()
    creator_id = models.UUIDField(null=False)

    class Meta:
        db_table = "project"

from common.models import TimeStampedModel
from django.db import models


class ProjectCollaborators(TimeStampedModel):

    project_id = models.ForeignKey(
        "Project",
        primary_key=True,
        on_delete=models.CASCADE,
        editable=False,
    )
    user_id = models.UUIDField(null=False)

    class Meta:
        db_table = "project_collaborators"
        unique_together = (("project_id", "user_id"),)

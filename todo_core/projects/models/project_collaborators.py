import uuid

from django.db import models

from common.models import TimeStampedModel
from projects.choices import ProjectCollaboratorRole


class ProjectCollaborators(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="collaborators"
    )
    user_id = models.UUIDField(null=False)

    role = models.CharField(
        max_length=1,
        choices=ProjectCollaboratorRole,
        default=ProjectCollaboratorRole.READER,
    )

    class Meta:
        db_table = "project_collaborators"
        unique_together = (("project_id", "user_id"),)

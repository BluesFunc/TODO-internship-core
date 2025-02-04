from common.models import TimeStampedModel
from django.db import models
from projects.choices.project_collaborator_role import ProjectCollaboratorRole


class ProjectCollaborators(TimeStampedModel):

    project_id = models.ForeignKey(
        "Project",
        primary_key=True,
        on_delete=models.CASCADE,
        editable=False,
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

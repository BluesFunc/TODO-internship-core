import uuid

from django.db import models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):

    id = models.UUIDField(
        primary_key=True,
    )
    name = models.CharField(max_length=300, null=False)
    description = models.TextField()
    creator_id = models.UUIDField(null=False)

    class Meta:
        db_table = "project"


class ProjectCollaborators(TimeStampedModel):

    project_id = models.ForeignKey(
        "Project",
        primary_key=True,
        on_delete=models.CASCADE,
        default=uuid.uuid4(),
        editable=False,
    )
    user_id = models.UUIDField(null=False)

    class Meta:
        db_table = "project_collaborators"
        unique_together = (("project_id", "user_id"),)

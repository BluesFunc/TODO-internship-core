from django.db import models
from django.utils.translation import gettext_lazy


class ProjectCollaboratorRole(models.TextChoices):
    READER = "R", gettext_lazy("Reader")
    EDITOR = "E", gettext_lazy("Editor")

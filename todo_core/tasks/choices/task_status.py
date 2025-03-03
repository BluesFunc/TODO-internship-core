from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy


class TaskStatus(models.TextChoices, Enum):
    TODO = "TD", gettext_lazy("To do")
    PROGRESS = "P", gettext_lazy("In progress")
    COMPLETE = "C", gettext_lazy("Complete")

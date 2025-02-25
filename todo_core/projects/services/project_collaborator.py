from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from projects.models import ProjectCollaborators


class ProjectCollaboratorsService:
    @staticmethod
    def create(collaborator: ProjectCollaborators) -> ProjectCollaborators:
        try:
            collaborator.save()
        except IntegrityError as ie:
            raise ValidationError(ie)
        return collaborator

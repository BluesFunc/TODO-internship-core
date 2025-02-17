from dataclasses import asdict

from django.db import IntegrityError
from projects.entities import ProjectCollaboratorEntity
from projects.models import ProjectCollaborators
from rest_framework.exceptions import ValidationError


class ProjectCollaboratorsService:
    @staticmethod
    def create(obj_data: ProjectCollaboratorEntity) -> ProjectCollaborators:
        try:
            data = asdict(obj_data)
            collaborator = ProjectCollaborators.objects.create(**data)
            return collaborator
        except IntegrityError as ie:
            raise ValidationError(ie)

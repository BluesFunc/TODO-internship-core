from django.db import IntegrityError

from common.exceptions import BadRequest
from projects.models import ProjectCollaborators


class ProjectCollaboratorsService:
    @staticmethod
    def create(collaborator: ProjectCollaborators) -> ProjectCollaborators:
        try:
            collaborator.save()
        except IntegrityError as ie:
            raise BadRequest(ie)
        return collaborator

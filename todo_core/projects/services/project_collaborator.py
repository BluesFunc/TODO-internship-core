from projects.models import ProjectCollaborat


class ProjectCollaboratorsService:
    @staticmethod
    def create(collaborator: ProjectCollaborators) -> ProjectCollaborators:
        collaborator.save()
        return collaborator

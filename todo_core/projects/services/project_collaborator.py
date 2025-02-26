from projects.models import ProjectCollaborators


class ProjectCollaboratorsService:
    @staticmethod
    def create(collaborator: ProjectCollaborators) -> ProjectCollaborators:
        collaborator.save()
        return collaborator

from rest_framework.serializers import (
    ChoiceField,
    ModelSerializer,
    PrimaryKeyRelatedField,
)

from projects.choices import ProjectCollaboratorRole
from projects.models import Project, ProjectCollaborators


class ProjectCollaboratorSerializer(ModelSerializer):

    project_id = PrimaryKeyRelatedField(queryset=Project.objects.all())
    role = ChoiceField(choices=ProjectCollaboratorRole.choices)

    class Meta:
        model = ProjectCollaborators
        fields = ["id", "project_id", "user_id", "role"]

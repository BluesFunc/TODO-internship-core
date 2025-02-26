from rest_framework import serializers

from projects.models import Project
from tasks.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "status",
            "deadline",
            "assigner_id",
            "project_id",
        ]

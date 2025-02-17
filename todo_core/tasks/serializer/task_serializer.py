from rest_framework import serializers
from tasks.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(read_only=True)

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

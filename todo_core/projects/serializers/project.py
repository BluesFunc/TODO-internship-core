from projects.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "creator_id"]
        extra_kwargs = {"creator_id": {"required": False}}

from rest_framework import viewsets

from .models.project import Project
from .serializers.project import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

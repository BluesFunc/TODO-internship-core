from rest_framework.viewsets import ModelViewSet

from .models.task import Task
from .serializer.task_serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

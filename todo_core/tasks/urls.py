from rest_framework_nested.routers import NestedDefaultRouter

from projects.urls import projects_router
from tasks.views import TaskViewSet

tasks_router = NestedDefaultRouter(projects_router, r"projects", lookup="project")
tasks_router.register(r"tasks", TaskViewSet, basename="project-tasks")

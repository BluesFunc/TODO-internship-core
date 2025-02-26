from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views.project import ProjectViewSet
from .views.project_collaborator import ProjectCollaboratorViewSet

projects_router = DefaultRouter()
projects_router.register(r"projects", ProjectViewSet, basename="project")


project_collaborator_router = NestedDefaultRouter(
    projects_router, r"projects", lookup="project"
)
project_collaborator_router.register(
    r"collaborators", ProjectCollaboratorViewSet, basename="project-collaborator"
)


urlpatterns = [
    *projects_router.urls,
    *project_collaborator_router.urls,
]

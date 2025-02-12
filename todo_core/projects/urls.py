from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views.project import ProjectViewSet
from .views.project_collaborator import ProjectCollaboratorViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)


project_collaborator_router = NestedDefaultRouter(router, r"projects", lookup="project")
project_collaborator_router.register(
    r"collaborators", ProjectCollaboratorViewSet, basename="project-collaborator"
)


urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(project_collaborator_router.urls)),
]

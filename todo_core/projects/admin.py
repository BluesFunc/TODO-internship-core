from django.contrib import admin

from .models.project import Project
from .models.project_collaborators import ProjectCollaborators

admin.site.register([Project, ProjectCollaborators])

import pytest

from projects.permissions import (
    IsCreateProjectPermission,
    IsProjectCollaboratorEditorPermission,
    IsProjectCollaboratorReaderPermission,
    IsProjectCreatorPermission,
    IsReadProjects,
)


@pytest.fixture
def project_collaborator_editor_permission() -> IsProjectCollaboratorEditorPermission:
    return IsProjectCollaboratorEditorPermission()


@pytest.fixture
def project_collaborator_reader_permission() -> IsProjectCollaboratorReaderPermission:
    return IsProjectCollaboratorReaderPermission()


@pytest.fixture
def create_project_permission() -> IsCreateProjectPermission:
    return IsCreateProjectPermission()


@pytest.fixture
def project_creator_permission() -> IsProjectCreatorPermission:
    return IsProjectCreatorPermission()


@pytest.fixture
def project_reader_permission() -> IsReadProjects:
    return IsReadProjects()

from typing import Type

import pytest

from projects.services import ProjectCollaboratorsService, ProjectService


@pytest.fixture()
def project_service_class() -> Type[ProjectService]:
    return ProjectService


@pytest.fixture()
def project_collaborator_class() -> Type[ProjectCollaboratorsService]:
    return ProjectCollaboratorsService

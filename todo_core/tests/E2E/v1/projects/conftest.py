from uuid import uuid4

import pytest
from tests.E2E.v1 import ProjectCollaboratorPayload, ProjectPayloadData

from projects.choices import ProjectCollaboratorRole
from projects.models import ProjectCollaborators


@pytest.fixture
def project_collaborator_url(project_instance_url: str) -> str:
    return project_instance_url + "collaborators/"


@pytest.fixture
def project_collaborator_instance_url(
    project_collaborator_url: str,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> str:
    return f"{project_collaborator_url}{project_collaborator_editor_instance.id}/"


@pytest.fixture
def project_collaborator_editor_payload() -> ProjectCollaboratorPayload:

    return ProjectCollaboratorPayload(
        user_id=str(uuid4()), role=ProjectCollaboratorRole.EDITOR.value
    )


@pytest.fixture
def project_collaborator_reader_payload() -> ProjectCollaboratorPayload:
    return ProjectCollaboratorPayload(
        user_id=str(uuid4()), role=ProjectCollaboratorRole.READER.value
    )


@pytest.fixture
def project_payload() -> ProjectPayloadData:

    return ProjectPayloadData(
        name="Project Payload",
        description="Test payload",
    )

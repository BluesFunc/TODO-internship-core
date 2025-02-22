from dataclasses import dataclass
from uuid import uuid4

import pytest
from projects.choices import ProjectCollaboratorRole
from projects.models import ProjectCollaborators


@dataclass
class ProjectCollaboratorPayload:
    user_id: str
    role: ProjectCollaboratorRole


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

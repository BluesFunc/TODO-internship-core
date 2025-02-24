from dataclasses import dataclass

import pytest
from tests import ProjectData, UserData


@dataclass(slots=True)
class ProjectPayloadData:
    name: str
    description: str


@pytest.fixture
def api_url_v1() -> str:
    return "/api/v1/"


@pytest.fixture
def project_url(api_url_v1: str) -> str:
    return api_url_v1 + "projects/"


@pytest.fixture
def project_instance_url(project_url: str, project_data: ProjectData) -> str:
    return f"{project_url}{project_data.id}/"


@pytest.fixture
def project_payload(full_permissions_valid_user_data: UserData) -> ProjectPayloadData:

    return ProjectPayloadData(
        name="Project Payload",
        description="Test payload",
    )

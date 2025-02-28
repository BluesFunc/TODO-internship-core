import pytest
from tests import ProjectData


@pytest.fixture
def api_url_v1() -> str:
    return "/api/v1/"


@pytest.fixture
def project_url(api_url_v1: str) -> str:
    return api_url_v1 + "projects/"


@pytest.fixture
def project_instance_url(project_url: str, project_data: ProjectData) -> str:
    return f"{project_url}{project_data.id}/"

import pytest
from django.conf import settings
from projects.models import Project, ProjectCollaborators


@pytest.fixture
def clinet_with_credentials(
    api_client,
):
    def _create_client(token_header: str):
        api_client.credentials(HTTP_AUTHORIZATION=token_header)
        return api_client

    return _create_client


@pytest.fixture
def invalid_client(clinet_with_credentials, token, token_signature):
    token_header = token_signature + token
    invalid_client = clinet_with_credentials(token_header)
    return invalid_client


@pytest.fixture
def valid_client(clinet_with_credentials, valid_user_token):
    valid_client = clinet_with_credentials("Bearer " + valid_user_token)
    return valid_client


@pytest.fixture
def api_url():
    return "/api/v1/"


@pytest.fixture
def project_url(api_url):
    return api_url + "projects/"


@pytest.fixture
def project_payload():

    payload = {
        "name": "Test Project",
        "description": "This is a test project",
    }
    return payload


@pytest.fixture(autouse=True)
def project_instance(db, valid_user_data) -> Project:
    creator_id = valid_user_data["user_id"]
    data = {"name": "Test Project", "description": "Test", "creator_id": creator_id}
    return Project.objects.create(**data)


@pytest.fixture(autouse=True)
def project_collaborator_instance(db, project_instance):
    user_id = project_instance.creator_id
    return ProjectCollaborators.objects.create(
        user_id=user_id, project_id=project_instance, role="E"
    )

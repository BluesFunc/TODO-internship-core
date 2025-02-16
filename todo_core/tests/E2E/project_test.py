import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_positive_project_create(
    valid_client: APIClient,
    project_url,
    project_payload,
):

    response = valid_client.post(project_url, project_payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_project_permissions_get(valid_client, project_url, project_instance):
    project_id = str(project_instance.id)
    url = f"{project_url+project_id}/"

    response = valid_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    response = valid_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_project_permissions_put(
    valid_client: APIClient, project_url, project_instance, project_payload
):

    project_id = str(project_instance.id)
    url = f"{project_url+project_id}/"

    response = valid_client.put(url, project_payload, format="json")
    print(response.__dict__)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_project_permissions_delete(
    valid_client,
    project_url,
    project_instance,
):
    project_id = str(project_instance.id)
    url = f"{project_url+project_id}/"

    response = valid_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.parametrize("token_signature", ["Bearer ", "Token ", ""])
@pytest.mark.parametrize(
    "token",
    ["", "1234", "invalid_user_token"],
)
@pytest.mark.django_db
def test_negative_project_create(
    invalid_client, project_url, project_instance, project_collaborator_instance
):

    data = {
        "name": "New Project",
        "description": "This is a new project",
    }

    response = invalid_client.post(project_url, data, format="json")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

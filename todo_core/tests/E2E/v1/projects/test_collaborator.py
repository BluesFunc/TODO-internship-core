from dataclasses import asdict

import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status
from rest_framework.test import APIClient
from tests.E2E.v1 import ProjectPayloadData

from projects.models import Project, ProjectCollaborators


@pytest.mark.parametrize(
    "payload",
    [
        lf("project_collaborator_editor_payload"),
        lf("project_collaborator_reader_payload"),
    ],
)
@pytest.mark.django_db
def test_positive_project_create(
    client_with_credentials: APIClient,
    project_collaborator_url: str,
    payload: ProjectPayloadData,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.post(
        project_collaborator_url, asdict(payload), format="json"
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.parametrize(
    "url", [lf("project_collaborator_instance_url"), lf("project_collaborator_url")]
)
@pytest.mark.django_db
def test_positive_project_get(
    client_with_credentials: APIClient,
    url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize(
    "payload",
    [
        lf("project_collaborator_editor_payload"),
        lf("project_collaborator_reader_payload"),
    ],
)
@pytest.mark.django_db
def test_positive_project_update(
    client_with_credentials: APIClient,
    project_collaborator_instance_url: str,
    payload: ProjectPayloadData,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.patch(
        project_collaborator_instance_url, asdict(payload), format="json"
    )

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_positive_project_delete(
    client_with_credentials: APIClient,
    project_collaborator_instance_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.delete(project_collaborator_instance_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

from dataclasses import asdict

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from tests.E2E.v1 import ProjectPayloadData

from projects.models import Project, ProjectCollaborators


@pytest.mark.django_db
def test_positive_project_create(
    client_with_credentials: APIClient,
    project_url: str,
    project_payload: ProjectPayloadData,
) -> None:

    response = client_with_credentials.post(
        project_url, asdict(project_payload), format="json"
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_project_get(
    client_with_credentials: APIClient,
    project_instance_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.get(project_instance_url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_project_patch(
    client_with_credentials: APIClient,
    project_instance_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    project_payload: ProjectPayloadData,
) -> None:

    response = client_with_credentials.patch(
        project_instance_url, asdict(project_payload), format="json"
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_project_delete(
    client_with_credentials: APIClient,
    project_instance_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    response = client_with_credentials.delete(project_instance_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

from dataclasses import asdict
from uuid import UUID, uuid4

import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status
from rest_framework.test import APIClient
from tests.E2E.v1.tasks import TaskData, TaskPayload

from projects.models import Project, ProjectCollaborators
from tasks.models import Task


@pytest.mark.parametrize(
    "request_url,expected_status,expected_value",
    [(lf("task_instance_url"), status.HTTP_200_OK, lf("task_instance_data"))],
)
@pytest.mark.django_db
def test_task_get(
    client_with_credentials: APIClient,
    request_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance: Task,
    expected_status: int,
    expected_value: TaskData,
) -> None:

    response = client_with_credentials.get(request_url)
    assert response.status_code == expected_status
    assert response.data["name"] == task_instance.name


@pytest.mark.parametrize(
    "request_url,expected_status,expected_value",
    [(lf("task_url"), status.HTTP_201_CREATED, lf("task_instance_data"))],
)
@pytest.mark.django_db
def test_task_create(
    client_with_credentials: APIClient,
    request_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance_payload: TaskPayload,
    expected_status: int,
    expected_value: TaskData,
) -> None:

    response = client_with_credentials.post(
        request_url, data=asdict(task_instance_payload), format="json"
    )
    assert response.status_code == expected_status
    assert response.data["name"] == expected_value.name


@pytest.mark.parametrize(
    "task_id,expected_status",
    [
        (lf("task_instance.id"), status.HTTP_204_NO_CONTENT),
        (uuid4(), status.HTTP_404_NOT_FOUND),
    ],
)
@pytest.mark.django_db
def test_task_delete(
    client_with_credentials: APIClient,
    task_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance_payload: TaskPayload,
    task_id: UUID,
    expected_status: int,
) -> None:
    request_url = f"{task_url}{task_id}/"
    response = client_with_credentials.delete(request_url)
    assert response.status_code == expected_status

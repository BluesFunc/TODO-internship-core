import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status
from rest_framework.test import APIClient

from projects.models import Project, ProjectCollaborators
from tasks.choices import TaskStatus
from tasks.models import Task, TaskStatusSubscribers


@pytest.mark.parametrize("expected_status", [status.HTTP_201_CREATED])
@pytest.mark.django_db
def test_subscribe_route(
    client_with_credentials: APIClient,
    task_subscribe_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance: Task,
    expected_status: int,
) -> None:
    response = client_with_credentials.post(task_subscribe_url, data={}, format="json")
    assert response.status_code == expected_status


@pytest.mark.parametrize("expected_status", [status.HTTP_204_NO_CONTENT])
@pytest.mark.django_db
def test_unsubscribe_route(
    client_with_credentials: APIClient,
    task_unsubscribe_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance: Task,
    task_status_subscriber_instance: TaskStatusSubscribers,
    expected_status: int,
) -> None:
    response = client_with_credentials.delete(task_unsubscribe_url)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    "task_status,expected_status", [(TaskStatus.TODO, status.HTTP_200_OK)]
)
@pytest.mark.django_db
def test_status_route(
    client_with_credentials: APIClient,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_status: TaskStatus,
    task_instance: Task,
    task_status_url: str,
    expected_status: int,
) -> None:
    response = client_with_credentials.patch(
        task_status_url, data={"status": task_status.name}, format="json"
    )
    assert response.status_code == expected_status
    if response.status_code == status.HTTP_200_OK:
        assert response.data["status"] == task_status.name


@pytest.mark.parametrize(
    "deadline,expected_status",
    [
        (lf("deadline_at_iso_format"), status.HTTP_200_OK),
        (lf("deadline_at_timestamp_format"), status.HTTP_400_BAD_REQUEST),
        ("invalid_time", status.HTTP_400_BAD_REQUEST),
    ],
)
@pytest.mark.django_db
def test_deadline_route(
    client_with_credentials: APIClient,
    task_deadline_url: str,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance: Task,
    expected_status: int,
    deadline: str,
) -> None:
    response = client_with_credentials.patch(
        task_deadline_url, data={"deadline": deadline}, format="json"
    )
    assert response.status_code == expected_status

from datetime import datetime

import pytest
from tests.E2E.v1.tasks import TaskData, TaskPayload

from tasks.models import Task


@pytest.fixture()
def task_url(project_instance_url: str) -> str:
    return f"{project_instance_url}tasks/"


@pytest.fixture()
def task_instance_url(task_url: str, task_instance: Task) -> str:
    return f"{task_url}{task_instance.id}/"


@pytest.fixture()
def task_subscribe_url(task_instance_url: str) -> str:
    return f"{task_instance_url}subscribe/"


@pytest.fixture()
def task_unsubscribe_url(task_instance_url: str) -> str:
    return f"{task_instance_url}unsubscribe/"


@pytest.fixture()
def task_deadline_url(task_instance_url: str) -> str:
    return f"{task_instance_url}deadline/"


@pytest.fixture()
def task_status_url(task_instance_url: str) -> str:
    return f"{task_instance_url}status/"


@pytest.fixture
def task_instance_data(task_instance: Task) -> TaskData:
    return TaskData(
        id=str(task_instance.id),
        name=task_instance.name,
        description=task_instance.description,
        status=task_instance.status,
        deadline=str(task_instance.deadline),
        assigner_id=str(task_instance.assigner_id),
        project_id=str(task_instance.project_id),
        created_at=str(task_instance.created_at),
    )


@pytest.fixture
def task_instance_payload(task_instance_data: TaskData) -> TaskPayload:
    return TaskPayload(
        name=task_instance_data.name,
        description=task_instance_data.description,
    )


@pytest.fixture
def deadline_at_iso_format(current_datetime_with_timezone: datetime) -> str:
    return current_datetime_with_timezone.isoformat()


@pytest.fixture
def deadline_at_timestamp_format(current_datetime_with_timezone: datetime) -> str:
    return str(current_datetime_with_timezone.timestamp())

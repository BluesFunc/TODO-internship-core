from dataclasses import asdict
from datetime import datetime, timezone
from unittest.mock import MagicMock
from uuid import UUID, uuid4

import pytest
from rest_framework.request import Request
from rest_framework.test import APIClient
from rest_framework.viewsets import GenericViewSet
from tests import JwtEncoder
from tests.utils import (
    MissingIdUserData,
    ProjectCollaboratorData,
    ProjectData,
    UserTokenPayload,
)

from common.choices import ProjectPermissions, Roles, TaskPermissions
from common.utils import UserData
from projects.choices import ProjectCollaboratorRole
from projects.models import Project, ProjectCollaborators
from tasks.models import Task, TaskStatusSubscribers


@pytest.fixture(scope="session")
def TokenEncoder() -> JwtEncoder:
    return JwtEncoder()


@pytest.fixture
def full_permissions_valid_user_payload() -> UserTokenPayload:

    return UserTokenPayload(
        mail="borov228@mail.ru",
        user_id="e1701363-5b69-4f08-a4bf-ce391fe0f11e",
        role=[Roles.user],
        permissions=[
            ProjectPermissions.create,
            ProjectPermissions.get,
            TaskPermissions.get,
            TaskPermissions.create,
        ],
    )


@pytest.fixture
def full_permissions_valid_user_data() -> UserData:

    return UserData(
        mail="borov228@mail.ru",
        user_id=UUID("e1701363-5b69-4f08-a4bf-ce391fe0f11e"),
        role=[Roles.user],
        permissions=[
            ProjectPermissions.create,
            ProjectPermissions.get,
            TaskPermissions.get,
            TaskPermissions.create,
        ],
    )


@pytest.fixture
def valid_user_data_without_permissions() -> UserData:
    return UserData(
        mail="borov228@mail.ru",
        user_id=UUID("2147f8f2-514b-441c-8841-0a5ca2b9c1b7"),
        role=[Roles.user],
        permissions=[],
    )


@pytest.fixture
def valid_user_data_without_test_project_access() -> UserData:
    return UserData(
        mail="borov228@mail.ru",
        user_id=uuid4(),
        role=[Roles.user],
        permissions=[
            ProjectPermissions.create,
            ProjectPermissions.get,
            TaskPermissions.get,
            TaskPermissions.create,
        ],
    )


@pytest.fixture()
def full_permission_valid_auth_user_token(
    full_permissions_valid_user_payload: UserTokenPayload, TokenEncoder: JwtEncoder
) -> str:
    return TokenEncoder.encode(full_permissions_valid_user_payload)


@pytest.fixture
def invalid_auth_user_data_without_user_id() -> MissingIdUserData:

    return MissingIdUserData(mail="borov228@mail.ru")


@pytest.fixture
def empty_auth_header() -> dict[str, str]:
    return {"": ""}


@pytest.fixture
def invalid_jwt_signature_auth_header() -> dict[str, str]:
    return {"Token ": ""}


@pytest.fixture
def invalid_jwt_auth_header() -> dict[str, str]:
    return {"Bearer ": "12345"}


@pytest.fixture
def missing_jwt_auth_header() -> dict[str, str]:
    return {"Bearer ": ""}


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def mock_request_without_user_data() -> MagicMock:
    request = MagicMock(Request)
    request.user_data = None
    return request


@pytest.fixture
def mock_auth_request(headers: dict[str, str]) -> MagicMock:
    request = MagicMock(spec=Request)
    request.headers = headers
    return request


@pytest.fixture
def mock_viewset() -> MagicMock:
    viewset = MagicMock(spec=GenericViewSet)
    return viewset


@pytest.fixture
def project_data(full_permissions_valid_user_data: UserData) -> ProjectData:

    return ProjectData(
        id=UUID("528a4d91-ef0a-452c-a28d-c9209df3c562"),
        name="Test",
        description="Test project",
        creator_id=full_permissions_valid_user_data.user_id,
    )


@pytest.fixture
def project_instance(project_data: ProjectData) -> Project:
    project = Project(**asdict(project_data))
    project.save()
    return project


@pytest.fixture()
def project_collaborator_editor_data(
    project_instance: Project, full_permissions_valid_user_data: UserData
) -> ProjectCollaboratorData:
    return ProjectCollaboratorData(
        user_id=full_permissions_valid_user_data.user_id,
        project_id=project_instance,
        role=ProjectCollaboratorRole.EDITOR.value,
    )


@pytest.fixture()
def project_collaborator_reader_data(
    project_instance: Project, full_permissions_valid_user_data: UserData
) -> ProjectCollaboratorData:
    return ProjectCollaboratorData(
        user_id=full_permissions_valid_user_data.user_id,
        project_id=project_instance,
        role=ProjectCollaboratorRole.READER.value,
    )


@pytest.fixture
def project_collaborator_editor_instance(
    project_collaborator_editor_data: ProjectCollaboratorData,
) -> ProjectCollaborators:
    collaborator = ProjectCollaborators(
        **asdict(project_collaborator_editor_data),
    )
    collaborator.save()
    return collaborator


@pytest.fixture
def project_collaborator_reader_instance(
    project_collaborator_reader_data: ProjectCollaboratorData,
) -> ProjectCollaborators:
    collaborator = ProjectCollaborators(
        **asdict(project_collaborator_reader_data),
    )
    collaborator.save()
    return collaborator


@pytest.fixture
def task_instance(
    project_instance: Project, full_permissions_valid_user_data: UserData
) -> Task:
    task = Task(
        name="Test",
        description="Test instance",
        project_id=project_instance,
        assigner_id=full_permissions_valid_user_data.user_id,
        deadline=datetime.now(timezone.utc),
    )
    task.save()
    return task


@pytest.fixture
def task_status_subscriber_instance(
    task_instance: Task, full_permissions_valid_user_data: UserData
) -> TaskStatusSubscribers:
    subscriber = TaskStatusSubscribers(
        user_id=full_permissions_valid_user_data.user_id, task_id=task_instance
    )
    subscriber.save()
    return subscriber


@pytest.fixture
def current_datetime_with_timezone() -> datetime:
    return datetime.now(timezone.utc)

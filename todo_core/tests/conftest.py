from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from typing import Callable
from unittest.mock import MagicMock
from uuid import uuid4

import jwt
import pytest
from projects.choices import ProjectCollaboratorRole
from projects.models import Project, ProjectCollaborators
from rest_framework.request import Request
from rest_framework.test import APIClient
from rest_framework.viewsets import GenericViewSet

from todo_core.settings import ALGORITHM, TOKEN_KEY


@dataclass(slots=True)
class UserData:
    mail: str | None
    user_id: str | None
    exp: datetime | None
    role: list[str] | None
    permissions: list[str] | None


@dataclass(slots=True)
class ProjectData:
    id: str | None
    name: str | None
    description: str | None
    creator_id: str | None


@dataclass(slots=True)
class ProjectCollaboratorData:
    user_id: str | None
    project_id: str | None
    role: ProjectCollaboratorRole | None


class JwtEncoder:
    key = TOKEN_KEY
    algorithm = ALGORITHM

    @classmethod
    def encode(cls, user_data: UserData) -> str:
        payload = asdict(user_data)
        return jwt.encode(payload=payload, key=cls.key, algorithm=cls.algorithm)


@pytest.fixture
def TOKEN_YEAR_EXPIRATION_TIME() -> timedelta:
    return timedelta(weeks=52)


@pytest.fixture
def TOKEN_SECOND_EXPIRATIONS_TIME() -> timedelta:
    return timedelta(seconds=1)


@pytest.fixture(scope="session")
def TokenEncoder() -> JwtEncoder:
    return JwtEncoder()


@pytest.fixture()
def get_current_time_with_time_zone() -> datetime:
    return datetime.now(tz=timezone.utc)


@pytest.fixture()
def token_expire_at(get_current_time_with_time_zone: datetime) -> Callable:
    def set_expirentaion_time(delta: timedelta) -> float:
        return (get_current_time_with_time_zone + delta).timestamp()

    return set_expirentaion_time


@pytest.fixture
def short_expirenation_time(
    TOKEN_SECOND_EXPIRATIONS_TIME: timedelta, token_expire_at: Callable
) -> datetime:

    return token_expire_at(TOKEN_SECOND_EXPIRATIONS_TIME)


@pytest.fixture
def long_expirenation_time(
    TOKEN_YEAR_EXPIRATION_TIME: timedelta, token_expire_at: Callable
) -> datetime:
    return token_expire_at(TOKEN_YEAR_EXPIRATION_TIME)


@pytest.fixture
def expired_auth_user_data(short_expirenation_time: datetime) -> UserData:
    return UserData(
        mail="borov228@mail.ru",
        user_id="e1701363-5b69-4f08-a4bf-ce391fe0f11e",
        exp=short_expirenation_time,
        role=["user"],
        permissions=["create_projects", "get_projects"],
    )


@pytest.fixture
def full_permissions_valid_user_data(long_expirenation_time: datetime) -> UserData:

    return UserData(
        mail="borov228@mail.ru",
        user_id="e1701363-5b69-4f08-a4bf-ce391fe0f11e",
        exp=long_expirenation_time,
        role=["user"],
        permissions=["create_projects", "get_projects"],
    )


@pytest.fixture
def valid_user_data_without_permissions(long_expirenation_time: datetime) -> UserData:

    return UserData(
        mail="borov228@mail.ru",
        user_id="2147f8f2-514b-441c-8841-0a5ca2b9c1b7",
        exp=long_expirenation_time,
        role=["user"],
        permissions=[],
    )


@pytest.fixture
def valid_user_data_without_test_project_access(
    long_expirenation_time: datetime,
) -> UserData:
    return UserData(
        mail="borov228@mail.ru",
        user_id=str(uuid4()),
        exp=long_expirenation_time,
        role=["user"],
        permissions=["create_projects", "get_projects"],
    )


@pytest.fixture
def invalid_auth_user_data_without_user_id() -> UserData:

    return UserData(
        mail="borov228@mail.ru", user_id=None, exp=None, role=None, permissions=None
    )


@pytest.fixture()
def full_permission_valid_auth_user_token(
    full_permissions_valid_user_data: UserData, TokenEncoder: JwtEncoder
) -> str:

    return TokenEncoder.encode(full_permissions_valid_user_data)


@pytest.fixture()
def valid_auth_user_token_without_permissions(
    valid_user_data_without_permissions: UserData, TokenEncoder: JwtEncoder
) -> str:
    return TokenEncoder.encode(valid_user_data_without_permissions)


@pytest.fixture
def invalid_auth_user_token(
    invalid_auth_user_data_without_user_id: UserData, TokenEncoder: JwtEncoder
) -> str:
    return TokenEncoder.encode(invalid_auth_user_data_without_user_id)


@pytest.fixture
def expired_auth_user_token(
    expired_auth_user_data: UserData, TokenEncoder: JwtEncoder
) -> str:

    return TokenEncoder.encode(expired_auth_user_data)


@pytest.fixture
def empty_auth_header() -> dict[str, str]:
    return {"": ""}


@pytest.fixture
def invalid_jwt_signature_auth_header() -> dict[str, str]:
    return {"Token ": ""}


@pytest.fixture
def expired_jwt_auth_header(expired_auth_user_token: str) -> dict[str, str]:
    return {"Bearer ": expired_auth_user_token}


@pytest.fixture
def invalid_jwt_auth_header() -> dict[str, str]:
    return {"Bearer ": "12345"}


@pytest.fixture
def missing_jwt_auth_header() -> dict[str, str]:
    return {"Bearer ": ""}


@pytest.fixture
def valid_jwt_auth_header(full_permission_valid_auth_user_token: str) -> dict[str, str]:
    return {"Bearer ": full_permission_valid_auth_user_token}


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def mock_request(request: pytest.FixtureRequest) -> MagicMock:
    mock_request = MagicMock(Request)
    mock_request.user_data = request.user_data
    return mock_request


@pytest.fixture
def mock_request_with_full_permission_user_data(
    full_permissions_valid_user_data: UserData,
) -> MagicMock:
    request = MagicMock(Request)
    request.user_data = asdict(full_permissions_valid_user_data)
    return request


@pytest.fixture
def mock_request_without_permissions_user_data(
    valid_user_data_without_permissions: UserData,
) -> MagicMock:
    request = MagicMock(Request)
    request.user_data = asdict(valid_user_data_without_permissions)
    return request


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
        id="528a4d91-ef0a-452c-a28d-c9209df3c562",
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
    project_data: ProjectData, full_permissions_valid_user_data: UserData
) -> ProjectCollaboratorData:
    return ProjectCollaboratorData(
        user_id=full_permissions_valid_user_data.user_id,
        project_id=project_data.id,
        role=ProjectCollaboratorRole.EDITOR.value,
    )


@pytest.fixture
def project_collaborator_editor_instance(
    project_collaborator_editor_data: ProjectCollaboratorData, project_instance: Project
) -> ProjectCollaborators:
    project_collaborator_editor_data.project_id = project_instance
    collaborator = ProjectCollaborators(
        **asdict(project_collaborator_editor_data),
    )
    collaborator.save()
    return collaborator

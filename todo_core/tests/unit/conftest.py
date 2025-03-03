from typing import Callable
from unittest.mock import MagicMock

import pytest
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from tests.conftest import ProjectData, UserData

from common.handlers import JwtHandler


@pytest.fixture
def mock_request_full_permission_user(
    full_permissions_valid_user_data: UserData,
) -> Request:
    request = MagicMock(spec=Request)
    request.user_data = full_permissions_valid_user_data
    return request


@pytest.fixture
def mock_request_user_without_permissions(
    valid_user_data_without_permissions: UserData,
) -> Request:
    request = MagicMock(spec=Request)
    request.user_data = valid_user_data_without_permissions
    return request


@pytest.fixture
def mock_request_user_without_test_project_access(
    valid_user_data_without_test_project_access: UserData,
) -> Request:
    request = MagicMock(spec=Request)
    request.user_data = valid_user_data_without_test_project_access
    return request


@pytest.fixture
def mock_project_viewset(
    project_data: ProjectData,
    mock_viewset: Callable,
) -> GenericAPIView:
    viewset = mock_viewset()
    viewset.kwargs = {"pk": str(project_data.id)}
    return viewset


@pytest.fixture
def mock_project_nested_viewset(
    project_data: ProjectData,
    mock_viewset: Callable,
) -> GenericAPIView:
    viewset = mock_viewset()
    viewset.kwargs = {"project_pk": str(project_data.id)}

    return viewset


@pytest.fixture(scope="session")
def TokenDecoder() -> JwtHandler:
    return JwtHandler()


@pytest.fixture
def mock_request_with_full_permission_user_data(
    full_permissions_valid_user_data: UserData,
) -> MagicMock:
    request = MagicMock(Request)
    request.user_data = full_permissions_valid_user_data
    return request


@pytest.fixture
def mock_request_without_permissions_user_data(
    valid_user_data_without_permissions: UserData,
) -> MagicMock:
    request = MagicMock(Request)
    request.user_data = valid_user_data_without_permissions
    return request


@pytest.fixture
def mock_request_with_project_reader_user_data() -> None:
    pass

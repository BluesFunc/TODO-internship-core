from typing import Callable
from unittest.mock import MagicMock

import pytest
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from tests.conftest import ProjectData, UserDataPayload

from common.handlers import JwtHandler


@pytest.fixture
def mock_request_full_permission_user(
    full_permissions_valid_user_data: UserDataPayload,
) -> Request:
    request = MagicMock(spec=Request)
    request.user_data = full_permissions_valid_user_data
    return request


@pytest.fixture
def mock_request_user_without_permissions(
    valid_user_data_without_permissions: UserDataPayload,
) -> Request:
    request = MagicMock(spec=Request)
    request.user_data = valid_user_data_without_permissions
    return request


@pytest.fixture
def mock_request_user_without_test_project_access(
    valid_user_data_without_test_project_access: UserDataPayload,
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
    viewset.kwargs = {"pk": project_data.id}
    return viewset


@pytest.fixture
def mock_project_nested_viewset(
    project_data: ProjectData,
    mock_viewset: Callable,
) -> GenericAPIView:
    viewset = mock_viewset()
    viewset.kwargs = {}
    viewset.kwargs["project_pk"] = project_data.id
    return viewset


@pytest.fixture(scope="session")
def TokenDecoder() -> JwtHandler:
    return JwtHandler()

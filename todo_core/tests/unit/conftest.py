from unittest.mock import MagicMock

import pytest
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


@pytest.fixture
def mock_request_authorized_user(valid_user_data: dict[str, str]) -> MagicMock:
    request = MagicMock(spec=Request)
    request.user_data = valid_user_data
    return request


@pytest.fixture
def mock_project_viewset(
    project_id: str,
    mock_viewset,
):
    viewset = mock_viewset()
    viewset.kwargs["project_pk"] = project_id
    return viewset

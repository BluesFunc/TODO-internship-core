from dataclasses import dataclass
from typing import Any
from unittest.mock import MagicMock

import pytest
from common.utils import decode_token, encode_payload
from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.viewsets import GenericViewSet


@dataclass(frozen=True)
class User:
    mail: str
    user_id: str


@pytest.fixture(scope="session")
def valid_user_data() -> dict[str, str]:

    data = {
        "mail": "borov228@mail.ru",
        "user_id": "e1701363-5b69-4f08-a4bf-ce391fe0f11e",
    }

    return data


@pytest.fixture
def invalid_user_data_without_user_id():
    invalid_data = {"mail": "borov228@mail.ru", "username": "PetyaAUF"}

    return invalid_data


@pytest.fixture
def valid_user_token(valid_user_data: dict[str, Any]) -> str:
    return encode_payload(valid_user_data)


@pytest.fixture
def invalid_user_token(invalid_user_data_without_user_id) -> str:
    return encode_payload(invalid_user_data_without_user_id)


@pytest.fixture
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def mock_request() -> MagicMock:
    request = MagicMock(Request)
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

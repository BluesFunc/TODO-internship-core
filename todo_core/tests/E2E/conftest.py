from typing import Callable

import pytest
from pytest import FixtureRequest
from pytest_lazy_fixtures import lf
from rest_framework.test import APIClient


@pytest.fixture
def auth_bearer_header(full_permission_valid_auth_user_token: str) -> str:
    return "Bearer " + full_permission_valid_auth_user_token


@pytest.fixture(params=[lf("auth_bearer_header")])
def client_with_credentials(
    api_client: APIClient, request: FixtureRequest
) -> APIClient:

    api_client.credentials(HTTP_AUTHORIZATION=request.param)
    return api_client


@pytest.fixture
def client_post_function(client_with_credentials: APIClient) -> Callable:
    return client_with_credentials.post


@pytest.fixture
def client_delete_function(client_with_credentials: APIClient) -> Callable:
    return client_with_credentials.delete

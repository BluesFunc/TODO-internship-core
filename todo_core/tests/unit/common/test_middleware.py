from typing import Callable
from unittest.mock import Mock

import pytest
from common.handlers import JwtHandler
from common.middleware import AuthMiddleware
from common.permissions import IsJwtAuthorizedPermisson
from django.http import HttpResponse
from pytest_lazy_fixtures import lf
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from tests import UserData


@pytest.mark.parametrize(
    "headers",
    [
        lf("empty_auth_header"),
        lf("invalid_jwt_signature_auth_header"),
        lf("expired_jwt_auth_header"),
        lf("invalid_jwt_auth_header"),
        lf("missing_jwt_auth_header"),
    ],
)
def test_auth_middleware(mock_auth_request: Callable, headers: str) -> None:
    mock_get_request = Mock(return_value=HttpResponse())
    middleware = AuthMiddleware(mock_get_request)
    mock_request = mock_auth_request(headers)

    response = middleware(mock_request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth_permission(
    mock_viewset: APIView,
    mock_request_with_full_permission_user_data: Request,
    mock_request_without_user_data: Request,
) -> None:
    permission = IsJwtAuthorizedPermisson()
    not_authorized_user = permission.has_permission(
        mock_request_without_user_data, mock_viewset
    )

    authorized_user = permission.has_permission(
        mock_request_with_full_permission_user_data, mock_viewset
    )

    assert not_authorized_user is False
    assert authorized_user is True


def test_token_decoder(
    valid_auth_user_token_without_permissions: str,
    TokenDecoder: JwtHandler,
    valid_user_data_without_permissions: UserData,
) -> None:
    data = TokenDecoder.decode_token(valid_auth_user_token_without_permissions)
    assert UserData(**data) == valid_user_data_without_permissions

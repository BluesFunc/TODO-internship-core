from unittest.mock import Mock

import pytest
from common.permissions import IsJwtAuthorizedPermisson
from common.utils import AuthMiddleware, decode_token, encode_payload
from django.http import HttpResponse
from rest_framework import status


def test_jwt_functions(valid_user_data: dict[str, str]):
    token = encode_payload(valid_user_data)
    data = decode_token(token)
    assert data == valid_user_data


@pytest.mark.parametrize(
    "headers",
    [
        {"Authorization": "Token 1234"},
        {"Authorization": "Bearer 2345"},
        {
            "Authorization": """Bearer eyJhbGciOiJIUzI1N
         iIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikp
         vaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKK
         F2QT4fwpMeJf36POk6yJV_adQssw5c"""
        },
    ],
)
def test_auth_middleware(mock_auth_request, headers):
    mock_get_request = Mock(return_value=HttpResponse())
    middleware = AuthMiddleware(mock_get_request)
    mock_request = mock_auth_request(headers)

    response = middleware(mock_request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth_permission(mock_viewset, mock_request):
    permission = IsJwtAuthorizedPermisson()
    has_permission = permission.has_permission(mock_request, mock_viewset)
    assert has_permission is False

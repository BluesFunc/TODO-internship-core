from typing import Any, Callable
from uuid import UUID

import jwt
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from rest_framework.exceptions import AuthenticationFailed

from common.handlers import JwtHandler
from common.utils import UserData


class AuthMiddleware:
    def __init__(self, get_response: Callable) -> None:

        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            token: str = request.META.get("HTTP_AUTHORIZATION")
            if not token:
                raise AuthenticationFailed(detail="Token is missing")
            if not token.startswith("Bearer "):
                raise AuthenticationFailed(detail="Wrong token signature")
            try:
                token = token.split()[1]
                data = JwtHandler.decode_token(token)
                user_data = self._parse_user_data(data)
            except IndexError:
                raise AuthenticationFailed("Required data is missing")
            except ValidationError:
                raise AuthenticationFailed("user id is invalid uuid")
            except jwt.DecodeError as e:
                raise AuthenticationFailed(e)
            except jwt.ExpiredSignatureError as e:
                raise AuthenticationFailed(e)
        except AuthenticationFailed as af:
            return HttpResponse(content=af, status=401)
        request.user_data = user_data
        response = self.get_response(request)
        return response

    def _parse_user_data(self, data: dict[str, Any]) -> UserData:
        user_data = UserData(
            mail=data["mail"],
            user_id=UUID(data["user_id"]),
            role=data["role"],
            permissions=data["permissions"],
        )
        return user_data

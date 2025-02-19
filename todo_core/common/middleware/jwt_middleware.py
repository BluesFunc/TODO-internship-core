from typing import Callable
from uuid import UUID

import jwt
from common.handlers import JwtHandler
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


class AuthMiddleware:

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> Response:
        token: str = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise AuthenticationFailed(detail="Token is missing")
        if not token.startswith("Bearer "):
            raise AuthenticationFailed(detail="Wrong token signature")

        try:
            token = token.split()[1]
            user_data = JwtHandler.decode_token(token)
            user_data["user_id"] = UUID(user_data["user_id"])
        except IndexError:
            raise AuthenticationFailed("Token is missing")
        except ValidationError:
            raise AuthenticationFailed("user id is invalid uuid")
        except jwt.DecodeError as e:
            raise AuthenticationFailed(e)
        except jwt.ExpiredSignatureError as e:
            raise AuthenticationFailed(e)
        except jwt.InvalidSignatureError as e:
            raise AuthenticationFailed(e)

        request.user_data = user_data
        response = self.get_response(request)
        return response

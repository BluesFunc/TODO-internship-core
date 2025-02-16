from typing import Callable

import jwt
from common.utils import decode_token
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response


class AuthMiddleware:

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: Request) -> Response:
        token: str = request.headers.get("Authorization", "")
        if not token.startswith("Bearer "):
            return HttpResponse("Wrong token signature", status=401)
        if not token:
            return HttpResponse("Token is missing", status=401)

        try:
            token = token[7:]
            user_data: dict[str, str] = decode_token(token)
        except jwt.DecodeError as e:
            return HttpResponse(e, status=401)
        except jwt.ExpiredSignatureError as e:
            return HttpResponse(e, status=401)
        except jwt.InvalidSignatureError as e:
            return HttpResponse(e, status=401)

        request.user_data = user_data
        response: Response = self.get_response(request)
        return response

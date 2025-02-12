from typing import Callable

import jwt
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.request import Request
from rest_framework.response import Response

from todo_core.settings import ALGORITHM, SECRET_KEY


class AuthMiddleware:

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: Request) -> Response:

        token: str = request.headers.get("Authorization", "")
        if not token.startswith("Bearer "):
            return HttpResponseBadRequest("Wrong token signature")
        if not token:
            return HttpResponse("Unauthorized", status=401)

        try:
            token = token[7:]
            user_data: dict[str, str] = jwt.decode(
                token, SECRET_KEY, algorithms=ALGORITHM
            )
        except jwt.DecodeError as e:
            return HttpResponseBadRequest(e)
        except jwt.ExpiredSignatureError as e:
            return HttpResponseBadRequest(e)
        except jwt.InvalidSignatureError as e:
            return HttpResponseBadRequest(e)

        request.user_data = user_data
        response: Response = self.get_response(request)
        return response

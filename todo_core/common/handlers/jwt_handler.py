from typing import Any

import jwt

from todo_core.settings import ALGORITHM, TOKEN_KEY


class JwtHandler:
    ALGORITHM = ALGORITHM
    TOKEN_KEY = TOKEN_KEY

    @staticmethod
    def decode_token(token: str) -> dict[str, Any]:
        return jwt.decode(token, key=TOKEN_KEY, algorithms=ALGORITHM)

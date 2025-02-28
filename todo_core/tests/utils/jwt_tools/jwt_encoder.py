from dataclasses import asdict

import jwt
from tests.utils import MissingIdUserData, UserTokenPayload

from todo_core.settings import ALGORITHM, TOKEN_KEY


class JwtEncoder:

    def __init__(self, key: str = TOKEN_KEY, algorithm: str = ALGORITHM) -> None:
        self.key = key
        self.algorithm = algorithm

    def encode(self, user_data: UserTokenPayload | MissingIdUserData) -> str:
        payload = asdict(user_data)
        return jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)

import jwt

from todo_core.settings import ALGORITHM, TOKEN_KEY


def encode_token(data: dict[str, str]) -> str:
    """
    encode jwt token from data
    """

    return jwt.encode(payload=data, key=TOKEN_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str:
    """
    decode jwt token
    """
    return jwt.decode(token, key=TOKEN_KEY, algorithms=ALGORITHM)

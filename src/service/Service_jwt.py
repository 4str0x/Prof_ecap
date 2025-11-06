from typing import Any, Union
from datetime import datetime, timedelta, timezone

from jwt import encode, decode, exceptions
from config.config import settings

from package.constant import *


class Token:
    """
    Class Token:
        Handles the creation and validation of tokens used in the authentication system.

    Methods:
        - create(document: dict) -> str:
            Generates a JWT based on the provided payload.

        - validate(jwt: str) -> dict:
            Validates a JWT and returns its payload or an error code.
    """

    def create(self, document: dict[str, Any]) -> str:
        """
        Creates a JWT with the given payload and expiration time.

        Args:
            document (dict): The payload to include in the token.

        Returns:
            str: The generated JWT.
        """
        current_utc_time = datetime.now(timezone.utc)  # Get the current date and time in UTC
        exp = current_utc_time + timedelta(minutes=int(settings.EXPIRES_IN))
        document.update({"exp": exp})
        document.update({"secret": settings.SECRET})

        Token_return = encode(
            payload=document, key=settings.JWT_SECRET_KEY, algorithm="HS256"
        )

        return Token_return

    def validate(self, jwt: str) -> dict[str, Union[str, dict[str, Any]]]:
        """
        Validates a JWT, checking its integrity and expiration.

        Args:
            jwt (str): The JWT to be validated.

        Returns:
            dict: A dictionary containing the validation status and, if valid, the token payload.
        """
        try:
            document = decode(
                jwt=jwt, key=settings.JWT_SECRET_KEY, algorithms=["HS256"]
            )

        except exceptions.DecodeError:
            return {"Code": INVALID_TOKEN_MSG}

        except exceptions.ExpiredSignatureError:
            return {"Code": EXPIRED_TOKEN_MSG}

        else:
            return {"Code": "Validate", "payload": document}

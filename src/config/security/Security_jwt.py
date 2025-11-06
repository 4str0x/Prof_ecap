from typing import Optional, Any

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from service.Service_jwt import Token
from package.constant import *
from config.config import settings

class JWTBearer(HTTPBearer):
    """
    Custom FastAPI security class for JWT validation using the HTTP Bearer authentication scheme.
    """

    def __init__(self, auto_error: bool = True) -> None:
        """
        Initializes the JWTBearer class.

        Args:
            auto_error (bool): Whether to automatically raise HTTP exceptions. Default is True.
        """
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:  # type: ignore
        """
        Overrides the HTTPBearer `__call__` method to validate incoming Bearer tokens.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Optional[str]: The JWT if validation passes.

        Raises:
            HTTPException: If the authentication scheme or token is invalid.
        """
        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(
            request
        )

        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )

            if not await self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid or expired token."
                )

            return credentials.credentials

        raise HTTPException(
            status_code=403, detail="Invalid authorization code."
        )

    async def verify_jwt(self, jwtoken: str) -> bool:
        """
        Verifies the validity of a JWT.

        Args:
            jwtoken (str): The JWT to be validated.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        token_instance = Token()

        # Validate the JWT
        token_data = token_instance.validate(jwtoken)
        if token_data["Code"] == EXPIRED_TOKEN_MSG:
            return False

        token_payload: dict[str, Any] = token_data.get("payload") #type: ignore
        if not token_payload:
            return False

        if token_payload.get("secret") == settings.SECRET:
            return True

        return False
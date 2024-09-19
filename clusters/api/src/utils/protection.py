from starlette import status
from fastapi import Depends, HTTPException
from core.routes.auth import token, db_queries
from core import oauth2_scheme


async def get_current_user(jwt_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    decoded_token = token.decode_access_token(jwt_token)
    if not decoded_token:
        raise credentials_exception
    user = await db_queries.get_user(decoded_token['user'])
    return user


__all__ = [
    'get_current_user'
]
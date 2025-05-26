from jose import jwt
from langgraph_sdk import Auth

import os

auth = Auth()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")


@auth.authenticate
async def authenticate(headers: dict):
    token = headers.get("x-user-token")
    if not token:
        raise Auth.exceptions.HTTPException(status_code=401, detail="Missing token")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return {"identity": payload["userId"], "is_authenticated": True}
    except Exception as e:
        raise Auth.exceptions.HTTPException(status_code=403, detail="Invalid token")


@auth.on
async def add_owner(ctx: Auth.types.AuthContext, value: dict):
    filters = {"owner": ctx.user.identity}
    metadata = value.setdefault("metadata", {})
    metadata.update(filters)
    return filters


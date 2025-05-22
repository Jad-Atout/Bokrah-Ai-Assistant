# auth.py
from langgraph_sdk import Auth
from jose import jwt, JWTError
import os

auth = Auth()

# Required environment variables
SECRET = os.environ["JWT_SECRET"]
ALGORITHM = os.environ["JWT_ALGORITHM"]
BEARER = os.environ["BEARER"]


def is_valid_key(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return "userId" in payload and "clientId" in payload
    except JWTError as e:
        print("JWT error:", e)
        return False


@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    # Normalize headers: decode and lowercase all keys
    headers = {k.decode().lower(): v.decode() for k, v in headers.items()}

    token = headers.get("x-api-key", "").replace(BEARER, "")
    print("AUTH HEADER:", token)

    if not is_valid_key(token):
        raise Auth.exceptions.HTTPException(
            status_code=401,
            detail="Invalid or missing JWT"
        )

    payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])

    return {
        "identity": payload["userId"],
        "role": payload.get("role", "user")
    }


async def configure(headers: dict) -> dict:
    # Normalize headers like in authenticate
    headers = {k.decode().lower(): v.decode() for k, v in headers.items()}

    token = headers.get("x-api-key", "").replace(BEARER, "")
    if not is_valid_key(token):
        return {}

    payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])

    return {
        "auth": {
            "client_id": payload["clientId"],
            "user_token": token,
            "role": payload.get("role", "user"),
            "org_id": payload.get("org_id")
        }
    }


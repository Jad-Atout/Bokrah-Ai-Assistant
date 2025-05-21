import os
import jwt
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, Header
from jwt.exceptions import InvalidTokenError
from graph import graph
from fastapi import FastAPI
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
app = FastAPI()


@app.post("/chat")
async def chat(request: Request, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization token missing or invalid")

    token = authorization.split(" ")[1]

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    # Extract values from the decoded payload
    user_id = decoded_token.get("userId")  # Adjust to your token structure
    client_id = decoded_token.get("clientId")  # Or "sub", or however it's stored

    body = await request.json()
    input_data = body.get("input", {})
    session_id = body.get("session_id", "default")

    result = graph.invoke(
        input_data,
        config={
            "configurable": {
                "thread_id": session_id,
                "user_id": user_id,
                "client_id": client_id,
                "user_token": token  # Optionally pass raw token for tools
            }
        }
    )
    return result

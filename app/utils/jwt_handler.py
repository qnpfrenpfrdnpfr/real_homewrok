import jwt
from datetime import datetime, timedelta

SECRET = "SECRET_KEY"

def create_token(payload: dict):
    payload["exp"] = datetime.utcnow() + timedelta(hours=12)
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        return None

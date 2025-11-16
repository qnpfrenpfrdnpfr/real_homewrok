from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
from app.utils.jwt_handler import verify_token

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    decoded = verify_token(token.credentials)
    if decoded is None:
        raise HTTPException(403, "Invalid token")
    return decoded   # { id: 1 }

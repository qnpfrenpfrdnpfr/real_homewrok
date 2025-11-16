from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user
from app.schemas.user_serviec import UserUpdate
from app.services.user_service import get_my_info, update_my_info

router = APIRouter(prefix="/user")

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return get_my_info(user["id"])

@router.put("/me")
def update_me(body: UserUpdate, user=Depends(get_current_user)):
    return update_my_info(user["id"], body)

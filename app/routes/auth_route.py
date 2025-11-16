from fastapi import APIRouter
from app.schemas.user_serviec import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth")

@router.post("/register") # post는 새 데이터 생성
def register(data: UserCreate):
    return register_user(data) 

@router.post("/login")
def login(data: UserLogin):
    return login_user(data)

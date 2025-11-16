from fastapi import HTTPException
from app.models.user_model import find_user_by_username, create_user, get_all_users
from app.utils.password_handler import hash_password, verify_password
from app.utils.jwt_handler import create_token

def register_user(data):
    if find_user_by_username(data.username):
        raise HTTPException(400, "Username already exists")

    users = get_all_users()
    new_id = (users[-1]["id"] + 1) if users else 1

    user_dict = {
        "id": new_id,
        "username": data.username,
        "password": hash_password(data.password),
        "email": data.email,
        "nickname": ""
    }

    create_user(user_dict)
    return {"message": "회원가입 성공", "user_id": new_id}

def login_user(data):
    user = find_user_by_username(data.username)
    if not user:
        raise HTTPException(400, "Invalid credentials")

    if not verify_password(data.password, user["password"]):
        raise HTTPException(400, "Invalid credentials")

    token = create_token({"id": user["id"]})
    return {"message": "로그인 성공", "token": token}

from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user
from app.schemas.post_service import PostCreate, PostUpdate
from app.services.post_service import *

router = APIRouter(prefix="/posts")

@router.get("/")
def list_all():
    return list_posts()

@router.get("/{pid}")
def detail(pid: int):
    return get_post_detail(pid)

@router.post("/")
def create(body: PostCreate, user=Depends(get_current_user)):
    return create_new_post(user["id"], body)

@router.put("/{pid}")
def update(pid: int, body: PostUpdate, user=Depends(get_current_user)):
    return update_existing_post(pid, user["id"], body)

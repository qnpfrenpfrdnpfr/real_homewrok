from fastapi import HTTPException
from app.models.post_model import get_all_posts, find_post, create_post, update_post

def list_posts():
    return get_all_posts()

def get_post_detail(pid: int):
    post = find_post(pid)
    if not post:
        raise HTTPException(404, "Post not found")
    return post

def create_new_post(uid, data):
    posts = get_all_posts()
    new_id = (posts[-1]["id"] + 1) if posts else 1

    post_dict = {
        "id": new_id,
        "title": data.title,
        "content": data.content,
        "author_id": uid
    }

    create_post(post_dict)
    return post_dict

def update_existing_post(pid, uid, data):
    post = find_post(pid)
    if not post:
        raise HTTPException(404, "Post not found")

    if post["author_id"] != uid:
        raise HTTPException(403, "No permission")

    return update_post(pid, data.dict(exclude_none=True))

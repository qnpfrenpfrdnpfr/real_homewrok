# app/models/post_model.py
from app.utils.file_handler import read_json, write_json

POST_FILE = "data/posts.json"

def get_all_posts():
    return read_json(POST_FILE)

def save_all_posts(data):
    write_json(POST_FILE, data)

def create_post(post_dict):
    posts = get_all_posts()
    posts.append(post_dict)
    save_all_posts(posts)

def find_post(post_id):
    posts = get_all_posts()
    for p in posts:
        if p["id"] == post_id:
            return p
    return None

def update_post(post_id, new_data):
    posts = get_all_posts()
    for i, p in enumerate(posts):
        if p["id"] == post_id:
            posts[i].update(new_data)
            save_all_posts(posts)
            return posts[i]
    return None

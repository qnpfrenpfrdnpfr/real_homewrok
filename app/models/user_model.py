# app/models/user_model.py
from app.utils.file_handler import read_json, write_json

USER_FILE = "data/users.json"

def get_all_users():
    return read_json(USER_FILE)

def save_all_users(data):
    write_json(USER_FILE, data)

def create_user(user_dict):
    users = get_all_users()
    users.append(user_dict)
    save_all_users(users)

def find_user_by_username(username):
    users = get_all_users()
    for u in users:
        if u["username"] == username:
            return u
    return None

def find_user_by_id(uid):
    users = get_all_users()
    for u in users:
        if u["id"] == uid:
            return u
    return None

def update_user(uid, new_data):
    users = get_all_users()
    for i, u in enumerate(users):
        if u["id"] == uid:
            users[i].update(new_data)
            save_all_users(users)
            return users[i]
    return None

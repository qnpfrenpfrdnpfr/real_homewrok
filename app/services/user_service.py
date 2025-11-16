from app.models.user_model import find_user_by_id, update_user

def get_my_info(uid: int):
    return find_user_by_id(uid)

def update_my_info(uid: int, data):
    new_data = data.dict(exclude_none=True)
    return update_user(uid, new_data)

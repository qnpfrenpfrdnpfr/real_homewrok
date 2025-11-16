from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    email: str | None = None
    nickname: str | None = None

class UserOut(BaseModel):
    id: int
    username: str
    email: str | None = None
    nickname: str | None = None

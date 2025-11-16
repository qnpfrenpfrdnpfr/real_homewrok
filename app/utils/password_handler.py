from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p): return pwd.hash(p)
def verify_password(raw, hashed): return pwd.verify(raw, hashed)

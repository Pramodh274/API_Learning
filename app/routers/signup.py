from fastapi import APIRouter, HTTPException
from app.models.user import SignupRequest
from app.utils.security import hash_password

router = APIRouter()

# In-memory user storage
users_db = {}


@router.post("/signup", status_code=201)
def signup(user: SignupRequest):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered.")
    users_db[user.email] = {
        "username": user.username,
        "password": hash_password(user.password),
    }
    return {"message": "User registered successfully!"}

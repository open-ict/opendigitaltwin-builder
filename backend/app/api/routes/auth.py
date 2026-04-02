from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings
from app.services.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(payload: LoginRequest):
    token = create_access_token(settings.SECRET_KEY, payload.email)
    return {"access_token": token, "token_type": "bearer"}

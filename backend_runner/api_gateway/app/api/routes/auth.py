from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["auth"])

class RegisterRequest(BaseModel):
    name: str
    role: str = "analyst"

@router.get("/me")
def get_me():
    return {
        "uid": "demo-uid",
        "email": "demo@danieth.com",
        "name": "Usuario Demo",
        "role": "analyst"
    }

@router.post("/auth/register")
def register_user(payload: RegisterRequest):
    return {
        "message": "Usuario registrado",
        "name": payload.name,
        "role": payload.role
    }
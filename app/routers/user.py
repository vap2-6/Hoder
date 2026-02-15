from fastapi import APIRouter, Depends
from ..dependencies import get_current_user

router = APIRouter()

@router.get("/profile")
def get_profile(user: dict = Depends(get_current_user)):
    return {
        "message": "User profile accessed",
        "user": user
    }

@router.get("/dashboard")
def user_dashboard(user: dict = Depends(get_current_user)):
    return {
        "message": "Welcome to user dashboard",
        "email": user["email"]
    }

from fastapi import APIRouter, Depends
from ..dependencies import require_admin

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard(admin: dict = Depends(require_admin)):
    return {
        "message": "Welcome to admin dashboard",
        "admin": admin
    }

@router.get("/stats")
def system_stats(admin: dict = Depends(require_admin)):
    return {
        "users": 100,
        "active_sessions": 42,
        "server_status": "healthy"
    }

from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from .database import engine, Base
from .routes import auth, user, admin
from .middleware import log_requests

# Create FastAPI app
app = FastAPI(title="Secure Cloud Backend")

# Create database tables
Base.metadata.create_all(bind=engine)

# RATE LIMITING SETUP
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests"}
    )

# MIDDLEWARE
app.middleware("http")(log_requests)

# ROUTES
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"status": "Secure Backend Running"}

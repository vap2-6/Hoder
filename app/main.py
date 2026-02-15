from fastapi import FastAPI
from .database import engine, Base
from .routes import auth, user, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Cloud Backend")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"status": "Secure Backend Running"}

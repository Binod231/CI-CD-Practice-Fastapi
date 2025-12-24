from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import engine
from app.models import user, task # Import models to create tables

# Create tables
user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CI/CD Practice"}

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI CI/CD Practice"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "supersecretkey" # Change this in production!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"

    class Config:
        env_file = ".env"

settings = Settings()

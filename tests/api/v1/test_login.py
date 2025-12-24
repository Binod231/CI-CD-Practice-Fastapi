from fastapi.testclient import TestClient
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.user import User
from sqlalchemy.orm import Session

def test_get_access_token(client: TestClient, db: Session):
    # Ensure user exists for login test
    email = "login_test@example.com"
    password = "password123"
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email, hashed_password=get_password_hash(password))
        db.add(user)
        db.commit()

    response = client.post(
        f"{settings.API_V1_STR}/login/access-token",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_incorrect_credentials(client: TestClient):
    response = client.post(
        f"{settings.API_V1_STR}/login/access-token",
        data={"username": "test@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401

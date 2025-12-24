from fastapi.testclient import TestClient
from app.core.config import settings

def test_create_user(client: TestClient):
    response = client.post(
        f"{settings.API_V1_STR}/users/",
        json={"email": "newuser@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert "id" in data

def test_create_existing_user(client: TestClient):
    # Create user first
    client.post(
        f"{settings.API_V1_STR}/users/",
        json={"email": "existing@example.com", "password": "password123"},
    )
    # Try to create again
    response = client.post(
        f"{settings.API_V1_STR}/users/",
        json={"email": "existing@example.com", "password": "password123"},
    )
    assert response.status_code == 400

def test_read_users_me(client: TestClient, normal_user_token_headers: dict):
    token = normal_user_token_headers["access_token"]
    response = client.get(
        f"{settings.API_V1_STR}/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"

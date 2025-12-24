from fastapi.testclient import TestClient
from app.core.config import settings

def test_create_task(client: TestClient, normal_user_token_headers: dict):
    token = normal_user_token_headers["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        f"{settings.API_V1_STR}/tasks/",
        headers=headers,
        json={"title": "Test Task", "description": "This is a test task"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert "id" in data
    assert "owner_id" in data

def test_read_tasks(client: TestClient, normal_user_token_headers: dict):
    token = normal_user_token_headers["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create a task first (optional, but good for robust test)
    client.post(
        f"{settings.API_V1_STR}/tasks/",
        headers=headers,
        json={"title": "Test Task 2", "description": "Another task"},
    )

    response = client.get(f"{settings.API_V1_STR}/tasks/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

import pytest
from FastAPI import app
from fastapi.testclient import TestClient
from FastAPI import todos


client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()


def test_get_todos() -> None:
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_post_todo() -> None:
    response = client.post("/todos", json={"title": "Ma tâche"})
    assert response.status_code == 200
    assert response.json() == {"id":None, "title":"Ma tâche", "completed":False}
import pytest
from FastAPI import app, User, Todo
from fastapi.testclient import TestClient
from FastAPI import todos
from FastAPI import users


client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_all():
    todos.clear()
    users.clear()


def test_get_users() -> None:
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_todos_by_id() -> None:
    user= User(user_id=1, username="Yaonn")
    users.append(user)
    todo= Todo (id=1, title="Ma tâche", completed=False, user_id=1)
    todos.append(todo)
    response = client.get("/users/1/todos")
    assert response.status_code == 200
    assert response.json() == [{"id":1, "title":"Ma tâche", "completed":False, "user_id":1}]


def test_user_without_todos() -> None:
    user = User(user_id=1, username="Yaonn")
    users.append(user)
    response = client.get("/users/1/todos")
    assert response.status_code == 200
    assert response.json() == []




def test_get_todos() -> None:
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_post_todo() -> None:
    response = client.post("/todos", json={"title": "Ma tâche"})
    assert response.status_code == 200
    assert response.json() == {"id":None, "title":"Ma tâche", "completed":False, "user_id":None}

def test_get_todos_by_id()-> None:
    todo=Todo(id=1, title="Ma tâche", completed=True, user_id=1)
    todos.append(todo)
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id":1, "title":"Ma tâche", "completed":True, "user_id":1}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class User(BaseModel):
	user_id: int
	username: str


class Todo(BaseModel):
	id: int
	title: str
	completed: bool = False
	user_id: int


users: list[User] = [
	User(user_id=1, username="Alice"),
	User(user_id=2, username="Bob"),
	User(user_id=3, username="Charlie"),
]

todos: list[Todo] = [
	Todo(id=1, title="Faire les courses", completed=False, user_id=1),
	Todo(id=2, title="Apprendre FastAPI", completed=True, user_id=1),
	Todo(id=3, title="Préparer la réunion", completed=False, user_id=2),
	Todo(id=4, title="Lire un livre", completed=False, user_id=3),
	Todo(id=5, title="Faire du sport", completed=True, user_id=2),
]


#new endpoints with user
#OK
@app.get("/users")
def read_users() -> list[User]:
	return users

#OK
@app.get("/users/{user_id}/todos")
def get_todos_user(user_id: int) -> list[Todo]:
	item_list: list[Todo] = []
	for item in todos:
		if item.user_id == user_id:
			item_list.append(item)
	return item_list


@app.post("/users/{user_id}/todos")
def add_todos_to_user(user_id: int, todo: Todo) -> Todo:
	for user in users:
		if user.user_id == user_id:
			todos.append(todo)
			return todo
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#OK
@app.put("/todos/{id}/toggle")
def toggle_completed(id: int) -> Todo:
	for item in todos:
		if item.id == id:
			item.completed = not item.completed
			return item
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#old endpoints:
@app.get("/")
def read_root() -> dict[str, str]:
	return {"message": "Hello World"}


@app.get("/todos")
def read_todos() -> list[Todo]:
	return todos


@app.post("/todos")
def add_todos(todo: Todo) -> Todo:
	todos.append(todo)
	return todo


@app.get("/todos/{id}")
def read_items(id: int) -> Todo:
	for item in todos:
		if item.id == id:
			return item
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.put("/todos/{id}")
def modify_item(id: int, todo: Todo) -> Todo:
	for item in todos:
		if item.id == id:
			item.title = todo.title
			item.completed = todo.completed
			return item
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/todos/{id}")
def delete_item(id: int) -> None:
	for item in todos:
		if item.id == id:
			todos.remove(item)
			return None
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

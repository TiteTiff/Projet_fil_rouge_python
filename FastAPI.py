from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status


app = FastAPI()

class Todo(BaseModel):
    id: int | None = None
    title: str
    completed: bool = False

todos:list[Todo]=[]

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/todos")
def read_todos() -> list[Todo]:
    return todos

@app.post("/todos")
def add_todos(todo: Todo)->Todo:
    todos.append(todo)
    return todo

@app.get("/todos/{id}")
def read_items(id:int) ->Todo:
    for item in todos:
        if item.id == id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.put("/todos/{id}")
def modify_item(id:int, todo:Todo)->Todo:
    for item in todos:
        if item.id == id:
            item.id=id
            item.title=todo.title
            item.completed=todo.completed
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.delete("/todos/{id}")
def delete_item(id:int)->None:
    for item in todos:
        if item.id == id:
            todos.remove(item)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
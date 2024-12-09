from fastapi import FastAPI

app = FastAPI()


todo_list = []


@app.get("/todos")
def get_todos():
    return todo_list

@app.post("/todos")
def create_todo(id: int, task: str, completed: bool = False):

    todo_list.append({"id": id, "task": task, "completed": completed})
    return {"message": "Todo item created"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, task: str, completed: bool):
    for item in todo_list:
        if item["id"] == todo_id:
            item["task"] = task
            item["completed"] = completed
            return {"message": "Todo item updated"}
    return {"message": "Todo item not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for item in todo_list:
        if item["id"] == todo_id:
            todo_list.remove(item)
            return {"message": "Todo item deleted"}
    return {"message": "Todo item not found"}

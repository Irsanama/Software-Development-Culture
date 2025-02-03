from fastapi import FastAPI, Path
from fastapi import Query

app = FastAPI()

items = [
    {"id": 1, "name": "item1"},
    {"id": 2, "name": "item2"},
    {"id": 3, "name": "item3"}
]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def get_items(skip: int = Query(0), limit: int = Query(10)):
    all_items = ["item1", "item2", "item3", "item4", "item5"]
    return {"items": all_items[skip : skip + limit]}

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(...)):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"Error": "Item not found"}
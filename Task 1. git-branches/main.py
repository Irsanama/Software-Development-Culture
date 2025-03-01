from fastapi import FastAPI, Path
from fastapi import Query

app = FastAPI()

all_items = [
    {"id": 1, "name": "item1", "description": "A fancy item", "price": 10.99},
    {"id": 2, "name": "item2", "description": "A useful item", "price": 5.49},
    {"id": 3, "name": "item3", "description": "A rare item", "price": 99.99},
    {"id": 4, "name": "item4", "description": "A common item", "price": 1.99},
    {"id": 5, "name": "item5", "description": "A premium item", "price": 49.99}
]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def get_items(skip: int = Query(0), limit: int = Query(10)):
    return {"items": all_items[skip : skip + limit]}

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(...)):
    for item in all_items:
        if item["id"] == item_id:
            return item
    return {"Error": "Item not found"}
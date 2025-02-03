from fastapi import FastAPI, Path

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
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(...)):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"Error": "Item not found"}
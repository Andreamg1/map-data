# api.py
from fastapi import FastAPI, HTTPException
from .crud import create_item, get_all_items, get_item_by_id
from .db import db
from .models import YourModel

app = FastAPI()

@app.post("/items/", response_model=YourModel)
def create_an_item(item: YourModel):
    return create_item(db.your_collection, item)

@app.get("/items/", response_model=List[YourModel])
def read_items():
    return get_all_items(db.your_collection)

@app.get("/items/{item_id}", response_model=YourModel)
def read_item(item_id: str):
    return get_item_by_id(db.your_collection, item_id)

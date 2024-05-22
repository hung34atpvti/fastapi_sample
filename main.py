from typing import Union, Annotated

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/fake_items_db")
async def query_param(skip: int = 0, limit: int = 10, short: Union[bool, int, str] = False, none: str = None):
    return {"message": fake_items_db[skip: skip + limit], "short": short, "none": none}


@app.get("/fake_items_db/{path_id}")
async def path_param(path_id: int):
    return {"message": fake_items_db[path_id]}


@app.post("/fake_items_db/")
async def create_item(item: Item):
    return item

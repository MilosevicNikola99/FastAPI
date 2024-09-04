from typing import Any

from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 15.5
    tags: list[str] = []


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str


items = [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

items1 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/items/")
async def create_item(item: Item) -> Item:
    items.append(item)
    return item

@app.post("/items/" , response_model=Item)
async def create_item1(item: Item) -> Any:
    items.append(item)
    return item

@app.get("/items/")
async def read_items() -> list[Item]:
    return items

#If you declare both a return type and a response_model, the response_model
# will take priority and be used by FastAPI.
@app.get("/items/", response_model=list[Item])
async def read_items1() -> Any:
    return items

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get("/items1/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items1[item_id]
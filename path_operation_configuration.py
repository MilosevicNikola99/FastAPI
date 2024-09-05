from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()



@app.get("/items/", tags=[Tags.items] ,
                         summary="Create an item",
                         description="Create an item with all the information, name, description, price, tax and a set of unique tags",
                         )
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users] , deprecated=True)
async def read_users():
    return ["Rick", "Morty"]

@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
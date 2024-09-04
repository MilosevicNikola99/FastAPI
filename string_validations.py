from typing import Annotated

from fastapi import FastAPI, Query
app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(title="Query string",
                                             description="Query string for the items to search in the database that have a good match",
                                             min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items1/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
from typing import Optional
from async_def import do_something
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    await do_something()
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    await do_something()
    return {"item_id": item_id, "q": q}

from fastapi import FastAPI

"""
run in terminal with -> uvicorn app:app --reload -> open broswer in http://127.0.0.1:8000/
check docs -> http://127.0.0.1:8000/docs#/
"""

app = FastAPI()

# 1.hello world
@app.get("/")
def root():
    return {"message": "hello world again"}


# 2.routes
@app.get("/users/{user_id}")
def read_user(user_id: int):  # can set to string, fastapi recognizes change
    """
    We accept a `user_id` here, and return a json-blob containing it.
    """
    return {"user_id": user_id}


# 3.json + 4. Type validation

from pydantic import BaseModel, validator


class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"Expected price >= 0, received {value}")
        return value


@app.post("/items/")
def create_item(item: Item):
    return item

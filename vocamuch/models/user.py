from pydantic import BaseModel


class Item(BaseModel):
    username: str
    password: str
    
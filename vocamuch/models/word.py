from pydantic import BaseModel


class Word(BaseModel):
    user_id: int
    word: str
    description: str
    
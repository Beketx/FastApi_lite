from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., min_length=20)
    last_name: str
    age: int = Field(..., gt=15,lt=90, description="less 15 and 90")

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError('Author age must be higher than 15')
    #     return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int
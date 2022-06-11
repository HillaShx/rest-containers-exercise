from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    name: str


class BookCreate(BookBase):
    author: str
    year_of_publication: int


class Book(BookBase):
    id: int
    author: str
    year_of_publication: int

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    id: int
    name: Optional[str]
    author: Optional[str]
    year_of_publication: Optional[int]

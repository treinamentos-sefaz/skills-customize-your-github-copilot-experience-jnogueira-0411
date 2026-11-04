from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}
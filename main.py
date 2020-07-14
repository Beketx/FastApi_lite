
from typing import List

from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author

app = FastAPI()
#
# @app.get('/')
# def home():
#     return {"key": "Hello"}
# @app.get('/{pk}')
# def get_item(pk: int, q: float=None):
#     return {"key": pk, "q": q}
#
# @app.get('/{pk}/user/{user}')
# def get_user(pk: int, user: float, item: str):
#     return {"key": pk, "Name number": user, "Item string": item}
#
# @app.get('/user/{pk}/item/{item}')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "items": item}

# @app.post('/book')
# def post_book(item: Book):
#     return item

@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], min_length=2, max_length=5, description="Search book")):
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages":  pages}

@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"item": item, "author": author, "quantity": quantity}

@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return author
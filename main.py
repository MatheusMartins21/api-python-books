from typing import List

from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str

app = FastAPI()

books: List[Book] = []

@app.get("/books")
async def getBooks(response: Response):
    if len(books) > 0:
        return books
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'Books not found.'}

@app.get("/books/{id}")
async def getBookById(id: int, response: Response):
    for book in books:
        if book.id == id:
            return book
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'The given id does not exist.'}

@app.post("/books")
async def createBook(book: Book):
    books.append(book)
    return books

@app.put("/books/{id}")
async def updateBookById(id: int, book: Book, response: Response):
    for index,bookIndex in enumerate(books):
        if bookIndex.id == id:
            books[index] = book
            return books[index]
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'The given id does not exist.'}

@app.delete("/books/{id}")
async def deleteBookById(id: int, response: Response):
    for index,bookIndex in enumerate(books):
        if bookIndex.id == id:
            del books[index]
            return books
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'The given id does not exist.'}

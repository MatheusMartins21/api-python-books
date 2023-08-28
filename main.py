from typing import List

from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    titulo: str
    autor: str

app = FastAPI()

books: List[Book] = []

@app.get("/livros")
async def getBooks(response: Response):
    if len(books) > 0:
        return books
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'Nenhum livro encontrado.'}

@app.get("/livros/{id}")
async def getBookById(id: int, response: Response):
    for book in books:
        if book.get('id') == id:
            return book
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': 'Livro não encontrado.'}

@app.post("/livros")
async def createBook(book: Book):
    books.append(book)
    return books

@app.put("/livros/{id}")
async def updateBookById(id: int, book: Book, response: Response):
    for index,bookIndex in enumerate(books):
        if bookIndex.get('id') == id:
            books[index].update(book)
            return books[index]
    response.status_code = status.HTTP_204_NOT_FOUND
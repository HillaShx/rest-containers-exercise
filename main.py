import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db_connection import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Nothing here. Go to locahlhost:8000/docs for the OpenAPI interface"}


@app.get("/books")
async def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)


@app.get("/books/<book_id>")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_by_id(db=db, book_id=book_id)


@app.post("/books")
async def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.put("/books")
async def update_book(book: schemas.BookUpdate, db: Session = Depends(get_db)):
    return crud.update_book(db=db, book=book)


@app.delete("/books/<book_id>")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db=db, book_id=book_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

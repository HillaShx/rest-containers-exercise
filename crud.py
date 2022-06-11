from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from utils import fields_to_update
import models
import schemas


def get_book_by_id(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(404)
    return book


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_user = models.Book(name=book.name, author=book.author, year_of_publication=book.year_of_publication)
    try:
        db.add(db_user)
        db.commit()
    except IntegrityError:
        raise HTTPException(409)
    db.refresh(db_user)
    return db_user


def update_book(db: Session, book: schemas.BookUpdate):
    book_record = get_book_by_id(db, book.id)
    if book_record is None:
        raise HTTPException(404)
    changed_fields = fields_to_update(book)
    db.query(models.Book).filter(models.Book.id == book.id).update(changed_fields)
    db.commit()
    return get_book_by_id(db, book.id)


def delete(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book is not None:
        db.delete(book)
        db.commit()

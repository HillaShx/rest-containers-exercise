from sqlalchemy import Column, Integer, String, UniqueConstraint
from db_connection import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    year_of_publication = Column(Integer)

    __table_args__ = (UniqueConstraint('name', 'author', 'year_of_publication', name='_book_row_uc'),)

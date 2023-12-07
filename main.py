from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import datetime  
from config import *


DATABASE_URL = "postgresql://"+user+":"+psw+"@localhost/"+db

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)  # Добавим значение по умолчанию для created_at

# Base.metadata.create_all(bind=engine)


# Создадим Pydantic-модель, используя sqlalchemy_to_pydantic
ItemPydantic = sqlalchemy_to_pydantic(Book, exclude=["id"])

def create_book(book_item: ItemPydantic):
    # Не нужно создавать новый экземпляр ItemPydantic, так как он уже получен как аргумент функции
    with SessionLocal() as db:
        book = Book(**book_item.dict())  # Установим created_at при создании книги
        db.add(book)
        db.commit()
        db.refresh(book)
    return book

def get_books():
    res = []
    with SessionLocal() as db:
        books = db.query(Book).all()
        for book in books:
            res.append({
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'created_at': book.created_at
            })
    return res

def retrieve_book(book_id):
    with SessionLocal() as db:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        return db_book

def update_book(book_id: int, book_data):
    with SessionLocal() as db:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book:
            # Обновим данные книги
            db_book.title = book_data['title']
            db_book.author = book_data['author']
            db_book.genre = book_data['genre']
            db.commit()
            db.refresh(db_book)
        return db_book
# print(update_book(2,  {"title": "Snow",
#     "author": "Lazy",
#     "genre": "mistery",
#     "created_at": "2020-05-01T02:09:03"}))

def delete_book(book_id):
    with SessionLocal() as db:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book:
            db.delete(db_book)
            db.commit()
        return db_book





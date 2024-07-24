from typing import Optional
from fastapi import FastAPI, Body, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status



app = FastAPI()

class book:
    id:int
    title:str
    description:str
    rating:int
    published_date:int
    def __init__(self,id,title,description,rating, published_date):
        self.id = id
        self.title = title
        self.description = description
        self.rating = rating
        self.published_date = published_date

class Book_request(BaseModel):
    id: Optional[int] = Field(description='id is not needed', default= None)  
    title:str = Field(min_length=3,max_length=10)
    description:str = Field(min_length=10)
    rating:int = Field(gt=-1,lt=6)
    published_date:int = Field(gt=1999,lt=2031)

    model_config = {                   
                       "json_schema_extra" : {
                              "example":{
                                     "title": " A new book",
                                     "description": "good to",
                                     "rating": 5,          
                                      "published_date":2029      
                         }

                    }
                  }


books = [  book(1,"Let us c","dse1",2,2025),
           book(2,"Let us java","dse2",1,2021),
           book(3,"Let us python","dse3",3,2022),
           book(4,"Let us C#","dse4",1,2014)
        ]


@app.get("/books", status_code=status.HTTP_200_OK)
def get_books():
    return books

@app.get("/book/{book_id}")
def read_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
          return book
    raise HTTPException(status_code=404,detail='item not find')
                    
@app.get("/books/published_date")
def read_by_published_date(published_date:int):
    return_published_date = []
    for book in books:
        if book.published_date == published_date:
            return_published_date.append(book)
    return return_published_date


@app.get("/books/find_by_rating")
def find_by_rating(rating:int = Query(gt=0,lt=5)):
    return_by_book =[]
    for book in books:
        if book.rating == rating:
            return_by_book.append(book)
    return return_by_book


    

    
 
@app.post("/books/create_new")
def create_new(newrecord = Body()):
    return books.append(newrecord)


@app.post("/books/create")
def create_book_pydantic(request_book:Book_request):
    return books.append(request_book)

@app.post("/books/")
def create_newbook_pydantic(request_book:Book_request):
    newbook = book(**request_book.model_dump())
    books.append(find_book_id(newbook))

def find_book_id(book1:book):
    book1.id = 1 if len(books) == 0 else books[-1].id + 1

    return book1
@app.put("/book2/update_book")
def update_record(book: Book_request):
     changed_book = False
     for i in range(len(books)):
        if books[i].id == book.id:
           books[i] = book
           changed_book = True
     if not changed_book:
         raise HTTPException(status_code=404,detail='item is not found')       

@app.delete("/book2/delete_record")
def delete_record(book: Book_request):
     for i in range(len(books)):
        if books[i].id == book.id:
           books.pop(i)
           break




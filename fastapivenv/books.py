from fastapi import Body, FastAPI

books = [
          {'title':'title_1', 'author':'author_1', 'category':'Science'},
          {'title':'title_2', 'author':'author_2', 'category':'Maths'},
          {'title':'title_3', 'author':'author_3', 'category':'English'},
          {'title':'title_4', 'author':'author_4', 'category':'CS'},
          {'title':'title_5', 'author':'author_5', 'category':'IT'},
]


app =FastAPI()
@app.get("/books/firstapi")
def firstapi():
    return books


@app.get("/books/{dynamic_param}")
def firstapi(dynamic_param:str):
    return {'dynamic_param':dynamic_param}


@app.get("/books/{book_category}")
def find_record(book_category:str):
    for book in books:
        if book.get('title').casefold() == book_category.casefold():
            return book


@app.get("/books/")
def book_record(book_category:str, book_author:str):
    return_record = []
    for book in books:
        if book.get('category').casefold() == book_category.casefold() and book.get('author').casefold() == book_author.casefold():
            return_record.append(book)
    return return_record


@app.post("/books/createbook")
def createbook(new_book=Body()):
    books.append(new_book)


@app.put("/books/updated_books")
def updated_books(updated_book = Body()):
    for i in range(len(books)):
        if books[i].get('category').casefold() == updated_book.get('category').casefold():
            books[i] = updated_book

@app.delete("/books/{deleted_record}")
def delete_record(deleted_record:str):
      for i in range(len(books)):
            if books[i].get('title').casefold() == deleted_record.casefold():
                books.pop(i)
                break







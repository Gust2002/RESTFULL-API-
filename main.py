from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/hello")
def Hello_world():
    return {"Message" "Hello guys"}


my_library = {}

class Book(BaseModel): 
    book_name: str 
    author_name:  str 
    book_year: int

@app.get("/request")
def get_book():
 if not my_library:
    return {"Message": "This book does not exist"}
 else:
     return {"get_book": my_library}
 
@app.post("/create")
def post_book(id_book: int, book: Book):
    if id_book in my_library:
        raise HTTPException(status_code=400,detail="This book is created already")
    else:
        my_library[id_book] = book.dict()
        return {"Message": "Your book has been created with suceafully!!"}
    

@app.put("/update/{id_book}")
def put_book(id_book: int, book: Book):
    my_book = my_library.get[id_book]
    if not my_book:
        raise HTTPException(status_code=404,detail="This book was not found on the system")
    else:
        my_book[id_book] = book.dict()
        return {"Message": "Your book has been update with sucesfully"} 



@app.delete("/delete/{id_book}")
def delete_book(id_book: int):
    if id_book not in my_library:
        raise HTTPException(status_code=500,detail="This book was not found on the system")
    else:
        del my_library[id_book]
        return {"Message": "Your book has been deleted with sucesfully"}
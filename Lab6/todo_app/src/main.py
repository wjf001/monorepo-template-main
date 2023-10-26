from fastapi import FastAPI, Body

app = FastAPI()

# Create a GET ReST API
@app.get("/api")
def first_api():
    return {"meg": "hello_world"}

# Create a GET ReST API with path parameters
@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}

# Create a GET ReST API with query parameters
@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}

# Create a POST ReST API
@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}

# Create a GET ReST API with path parameters AND query parameters
@app.get("/items/{item_id}")
def first_apiV5(item_id: str, name: str):
    return {"item_id": item_id, "name": name}


# Create a PUT ReST API
items = {
    1: {"name": "Item 1", "description": "Description 1"},
    2: {"name": "Item 2", "description": "Description 2"},
}
@app.put('/items/{item_id}')
def first_apiV6(item_id: int, updated_item: dict):
    items[item_id] = updated_item
    return {"msg": "Item updated"}


# Create a DELETE ReST API
@app.delete("/items/{item_id}")
def first_apiV7(item_id: str):
    return {"message": "Item deleted"}


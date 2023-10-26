from fastapi.testclient import TestClient
from todo_app.src.main import app

client = TestClient(app)

def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"meg": "hello_world"}

def test_first_apiV2():
    response = client.get("/books/some_param")
    assert response.status_code == 200
    assert response.json() == {"msg": "some_param"}

def test_first_apiV3():
    response = client.get("/books/?title=some_title")
    assert response.status_code == 200
    assert response.json() == {"msg": "some_title"}

def test_first_apiV4():
    response = client.post("/books/create_book", json={"key": "value"})
    assert response.status_code == 200
    assert response.json() == {"msg": {"key": "value"}}

def test_first_apiV5():
    response = client.get("/items/123?name=John")
    assert response.status_code == 200
    assert response.json() == {"item_id": "123", "name": "John"}

def test_first_apiV6():
    response = client.put("/items/1", json={"name": "Updated Item", "description": "Updated Description"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Item updated"}

def test_first_apiV7():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}


from fastapi.testclient import TestClient
from main import app  # Ensure `main.py` correctly exposes `app`

client = TestClient(app)  # Initialize test client

def test_get_all_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response is a list

def test_get_single_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "author" in data

def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/api/v1/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == new_book["title"]

def test_update_book():
    updated_book = {
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/api/v1/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_book["title"]

def test_delete_book():
    response = client.delete("/api/v1/books/3")
    assert response.status_code == 204  # No Content

    response = client.get("/api/v1/books/3")
    assert response.status_code == 404  # Not Found

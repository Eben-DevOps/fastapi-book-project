from fastapi.testclient import TestClient
from main import app
from core.config import settings  # Import settings for API prefix

client = TestClient(app)
API_PREFIX = settings.API_PREFIX  # Ensure correct API prefix

def test_get_all_books():
    response = client.get(f"{API_PREFIX}/books/")  # ✅ Use correct prefix
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)  # ✅ Ensure response is a dict

    book_list = list(data.values())  # ✅ Convert dict to list
    assert isinstance(book_list, list)
    assert len(book_list) == 3

def test_get_single_book():
    response = client.get(f"{API_PREFIX}/books/1")  # ✅ Correct path
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
    response = client.post(f"{API_PREFIX}/books/", json=new_book)  # ✅ Use correct prefix
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == new_book["title"]

def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put(f"{API_PREFIX}/books/1", json=updated_book)  # ✅ Correct prefix
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_book["title"]

def test_delete_book():
    response = client.delete(f"{API_PREFIX}/books/3")  # ✅ Correct prefix
    assert response.status_code == 204

    response = client.get(f"{API_PREFIX}/books/3")
    assert response.status_code == 404

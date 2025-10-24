import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_news():
    response = client.get("/news")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)

    if data:
        item=data[0]
        assert "_id" in item
        assert "title" in item
        assert "link" in item
        assert "published" in item


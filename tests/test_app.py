from fastapi.testclient import TestClient
from bingo_server.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bingo server is up and running!"}
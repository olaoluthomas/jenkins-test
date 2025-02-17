# test_app.py
import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Jenkins!' in response.data

def test_add(client):
    response = client.get('/add/3/4')
    assert response.status_code == 200
    assert b'7' in response.data

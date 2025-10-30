"""Tests for FastAPI backend"""

from fastapi.testclient import TestClient
from app.main import app  # Importing the main application

# Creating the test client
client = TestClient(app)


def test_root_endpoint_returns_200():
    """Test that root endpoint returns 200 status code"""
    response = client.get("/")
    assert response.status_code == 200


def test_root_endpoint_returns_correct_message():
    """Test that root endpoint returns correct welcome message"""
    response = client.get("/")
    assert response.json() == {"message": "Welcome to this Assignment"}


def test_health_endpoint_returns_200():
    """Test that health endpoint returns 200 status code"""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_returns_correct_status():
    """Test that health endpoint returns correct status value"""
    response = client.get("/health")
    assert response.json() == {"status": "200_OK"}


def test_non_existing_endpoint():
    """Test that if user try to get a non-existing endpoint retuens true exception"""
    response = client.get("/test_somthing")
    assert response.json() == {
        "error": True,
        "status_code": 404,
        "detail": "Not Found",
        "path": "/test_somthing",
    }

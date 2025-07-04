import pytest
from app.main import getapp
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def client() -> TestClient:
    app = getapp()
    client = TestClient(app)

    return client

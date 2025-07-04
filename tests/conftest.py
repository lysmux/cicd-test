import pytest
from fastapi.testclient import TestClient

from app.main import getapp


@pytest.fixture(scope="session")
def client() -> TestClient:
    app = getapp()
    client = TestClient(app)

    return client

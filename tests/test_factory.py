from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app(TestConfig).testing


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"

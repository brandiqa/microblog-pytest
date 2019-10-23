from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True


def test_config():
    # create_app without passing config shouldn't be in test mode
    assert not create_app().testing

    # create_app with {TESTING = True} config should run in test mode
    assert create_app(TestConfig).testing


def test_hello(client):
    # Route /hello should return the text "Hello, World!"
    response = client.get("/hello")
    assert response.data == b"Hello, World!"

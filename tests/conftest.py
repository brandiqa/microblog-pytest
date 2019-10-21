import pytest
from app import create_app, db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


@pytest.fixture
def app():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app

    # close and remove the temporary database
    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)

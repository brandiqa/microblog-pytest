import pytest
from app import create_app, db
from app.models import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SERVER_NAME = 'localhost.test'
    WTF_CSRF_ENABLED = False


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
    return app.test_client()


@pytest.fixture
def req_ctx(app):
    with app.test_request_context() as ctx:
        yield ctx


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client
        # Initialize Test User
        u = User(username='test', email='test@example.com')
        u.set_password('test')
        db.session.add(u)
        db.session.commit()

    def login(self, username="test", password="test", redirect=True):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password},
            follow_redirects=redirect
        )

    def logout(self, redirect=True):
        return self._client.get("/auth/logout", follow_redirects=redirect)

    def register(self, username, email, password, password2, redirect=True):
        return self._client.post('/auth/register',
                                 data=dict(username=username,
                                           email=email,
                                           password=password,
                                           password2=password2),
                                 follow_redirects=redirect)


@pytest.fixture
def auth(client):
    return AuthActions(client)

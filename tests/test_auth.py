from conftest import auth

def test_login(client, auth):
    # test login page renders without template renders
    assert client.get("/auth/login").status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "http://localhost/"


def test_register(client, auth):
    # test register page renders without template renders
    assert client.get("/auth/register").status_code == 200
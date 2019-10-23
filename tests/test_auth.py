# def login(client, username, password):
#     return client.post('/auth/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)


# def logout(client):
#     return client.get('/auth/logout', follow_redirects=True)


def test_login_logout(client, auth, test_user):
    # Ensure test user exists in the database
    assert test_user.id == 1

    # Confirm login page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # Test invalid username
    response = auth.login('test123', 'test')
    assert b'Invalid username or password' in response.data

    # Test invalid password
    # response = login(client, 'test', 'test123')
    response = auth.login('test', 'test123')
    assert b'Invalid username or password' in response.data

    # Test valid username and password
    # response = login(client, 'test', 'test')
    response = auth.login()
    assert b'Hi, test!' in response.data

    # Test logout route
    response = auth.logout()
    assert b'Please log in to access this page.' in response.data
    assert b'Sign In' in response.data

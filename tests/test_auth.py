def test_login_logout(client, auth):
    # Login page should render without template errors
    assert client.get("/auth/login").status_code == 200

    # Invalid username should display flash message
    response = auth.login('test123', 'test')
    assert b'Invalid username or password' in response.data

    # Invalid password should display flash message
    response = auth.login('test', 'test123')
    assert b'Invalid username or password' in response.data

    # Successful login should redirect to home page with user greeting
    response = auth.login()
    assert b'Hi, test!' in response.data

    # Successful logout should redirect to login page
    response = auth.logout()
    assert b'Please log in to access this page.' in response.data
    assert b'Sign In' in response.data

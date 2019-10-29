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
    assert response.headers['Location'] == 'http://localhost/'

    # Authenticated users shouldn't access login pages
    response = client.get('/auth/login', follow_redirects=True)
    assert b'Hi, test!' in response.data

    # Successful logout should redirect to login page
    response = auth.logout()
    assert b'Please log in to access this page.' in response.data
    assert b'Sign In' in response.data


def register(client, username, email, password, password2):
    return client.post('/auth/register',
                       data=dict(username=username,
                                 email=email,
                                 password=password,
                                 password2=password2),
                       follow_redirects=True)


def test_registration(client, auth):
    # Registration page should render without template errors
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Register' in response.data

    # Blank field values should not submit
    response = client.post('/auth/register', follow_redirects=True)
    assert b'This field is required' in response.data

    # Duplicate username should display error message
    response = register(client, "test", "test@example.com", "test", "test")
    assert b'Please use a different username' in response.data
    assert b'Please use a different email address' in response.data

    # Unmatching passwords should not submit
    response = register(client, "susan", "susan@example.com", "cat1", "cat2")
    assert b'Field must be equal to password' in response.data

    # Unique username, matching passwords should succeed & redirect to login
    response = register(client, "susan", "susan@example.com", "cat", "cat")
    assert b'Congratulations, you are now a registered user!' in response.data
    assert b'Sign In' in response.data
    # assert response.location == 'http://localhost/auth/login'

    # Authenticated users shouldn't access register page
    response = auth.login('susan', 'cat')
    assert b'Hi, susan!' in response.data
    response = client.get('/auth/register', follow_redirects=True)
    assert b'Hi, susan!' in response.data

from flask import url_for


def post(client, post, redirect=False):
    return client.post(url_for('main.index'),
                       data={"post": post},
                       follow_redirects=redirect)


def test_posts(client, auth):
    # unautheticated user should NOT access home page
    response = client.get(url_for('main.index'))
    assert response.status_code == 302
    assert response.location == 'http://localhost.test/auth/login?next=%2Findex'

    # unauthenticated user should NOT be allowed to post
    response = post(client, "This is a random message")
    assert response.status_code == 302
    assert response.location == 'http://localhost.test/auth/login?next=%2Findex'

    # unautheticated user should NOT access explore page
    response = client.get(url_for('main.explore'))
    assert response.status_code == 302
    assert response.location == 'http://localhost.test/auth/login?next=%2Fexplore'

    # authenticated user should access home page
    auth.login()
    response = client.get(url_for('main.index'), follow_redirects=True)
    assert b'Hi, test!' in response.data
    assert b'This is a random message' not in response.data

    # authenticated user should be allowed to post
    response = post(client, "This is a random message", True)
    assert b'This is a random message' in response.data

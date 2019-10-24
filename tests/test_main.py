from flask import url_for


def test_posts(client, auth):
    # should not access posts without logging in
    response = client.get(url_for('main.index'), follow_redirects=True)
    assert b'Sign In' in response.data

    # should access home page as logged in user
    auth.login()
    response = client.get(url_for('main.index'), follow_redirects=True)
    assert b'Hi, test!' in response.data
    assert b'This is a random message' not in response.data

    # should post random message
    response = client.post(url_for('main.index'),
                           data={"post": "This is a random message"},
                           follow_redirects=True)
    assert b'This is a random message' in response.data

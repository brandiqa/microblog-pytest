# Microblog - Pytest Example

This is a slightly modified version of the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). This Flask-Pytest example project is part of a tutorial that teaches developers how to write tests for Flask using `pytest`. See [Sitepoint artice](https://www.sitepoint.com).


## Setup

Install Python 3 on your system if it's missing. On Linux, use `python3`. Python 2.7 is deprecated.

Open a new terminal:

```bash
# Clone Project
git clone git@github.com:brandiqa/microblog-pytest.git
cd microblog-pytest

# Setup and activate project environment
python -m venv venv
source venv/bin/activate

# Upgrade pip and install project dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initialize Flask database
flask db upgrade

# Sartup Flask server
flask run
```

## Testing

```bash
# Switch to testing branch
git checkout testing

# Install Pytest
pip install pytest

# Run Pytest
PYTHONPATH=. pytest -v
```

## Coverage

```bash
# Install
pip install pytest-cov

# Run test coverage tool
pytest --cov=app tests/

# Generate html report
pytest --cov-report html --cov=app tests/
```

## LICENSE

The MIT License (MIT)

Copyright (c) 2017 Miguel Grinberg

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
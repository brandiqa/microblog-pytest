# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

# Setup

Install Latest version of Python (current is 3.8)

alias python="python3.8"

Open a new terminal:

```bash
git clone ....

cd {}

python -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

flask db upgrade

flask run
```

# Testing

```bash
pip install pytest

pip install -e .

pytest
```
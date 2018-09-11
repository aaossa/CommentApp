from os import environ, path
from secrets import token_hex


__basedir = path.abspath(path.dirname(__file__))

# Main
DEBUG = False

# Secrets
SECRET_KEY = environ.get("FLASK_SECRET_KEY", token_hex(64))

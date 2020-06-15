# pypi
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    return app


HOME_PAGE = "/"
TITLE = "Bug-Jar"

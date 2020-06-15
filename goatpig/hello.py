# from pypi
# from flask import Flask, render_template
from flask import render_template

# app = Flask(__name__)

from goatpig import create_app, HOME_PAGE, TITLE

app = create_app()

@app.route(HOME_PAGE)
def hello_world():
    return render_template("hello.html", title=TITLE)

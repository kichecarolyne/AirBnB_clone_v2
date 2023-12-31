#!/usr/bin/python3
""" Start a Flask web application listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!", /hbnb: display "HBNB", /c/<text>:
display c followed by text, /python/(<text>): display python, followed text
default text value "is cool"
Must use strict_slashes=False in route definition """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Display "HBNB" """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ Display C followed by text variable """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """ Display text variable """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

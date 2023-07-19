#!/usr/bin/python3
"""
Write a script that starts a Flask application
Your app must be listening on 0.0.0.0, port 5000

Routes:
    - /: display "Hello HBNB!"
    - /hbnb: display "HBNB"
    - /r/<text>: diaplay "C" folloewed by the value of the text variable
    (replace underscore _ with a space

Note: you must use the option strict_slashes=False in your route defintion
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
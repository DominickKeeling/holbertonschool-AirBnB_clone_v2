#!/usr/bin/python3
"""
Write a script that starts a flask application

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable
    - /python/<text>: display “Python”, followed by the value of the text var
    - /number/<n>: display "n is a number" only if n is an integer

Note: You must use the option strict_slashes=False in route definition
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

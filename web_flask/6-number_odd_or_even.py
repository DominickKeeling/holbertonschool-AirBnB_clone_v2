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
    - /number_template/<n>: display a HTML page only if n is an integer
        H1 tag: "Number: n" inside the tag BODY
    - /number_odd_or_even/<n>: Display an HTML page only if n is an integer
        H1 tag: "Number: n is even|odd" inside the tag BODY

Note: You must use the option strict_slashes=False in route definition
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display HELLO HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays C followed by text """
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ Displays Python followed by text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Displays 'n is a number' """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Displays number template if n is a number """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ Displays a number and whether its even or odd """
    odd_or_even = 'odd' if n %2 else 'even'
    return render_templates('6-odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

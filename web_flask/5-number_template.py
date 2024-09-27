#!/usr/bin/python3
"""
A simple Flask web application with multiple routes, including an HTML template route.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route that returns 'C' followed by the text passed in the URL.
       Underscores in the text are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route that returns 'Python' followed by the text passed in the URL.
       Underscores in the text are replaced with spaces.
       If no text is provided, the default is 'is cool'.
    """
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Route that returns 'n is a number' if n is an integer."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route that returns an HTML page with 'Number: n' if n is an integer."""
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

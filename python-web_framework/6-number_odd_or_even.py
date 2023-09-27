#! /usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        result = '{} is even'.format(n)
    else:
        result = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

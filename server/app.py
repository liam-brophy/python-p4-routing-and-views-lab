#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter, file=sys.stdout)
    return parameter

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
    count_str = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count_str

@app.route('/math/<int:param1>/<operator>/<int:param2>')
def math_route(param1, operator, param2):
    if operator == '+':
        result = param1 + param2
    elif operator == '-':
        result = param1 - param2
    elif operator == '*':
        result = param1 * param2
    elif operator == 'div':
        result = param1 / param2
    elif operator == '%':
        result = param1 % param2
    else:
        return "Invalid operator", 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

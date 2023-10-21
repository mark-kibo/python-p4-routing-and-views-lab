#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:value>")
def print_string(value):
    print(value)
    return f"{value}"
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(0, parameter + 1)
    return '<br>'.join(map(str, numbers))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."

    return f"{result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)

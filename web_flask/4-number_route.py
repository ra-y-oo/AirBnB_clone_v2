#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    formatted = text.replace('_', ' ')
    return f"C {formatted}"

@app.route("/pythons/(<text>)", strict_slashes=False)
def python(text):
    text = "is cool"
    formatted = text.replace('_','')
    return f"Python {formatted}"

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n} is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

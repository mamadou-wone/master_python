from flask import Flask
from markupsafe import escape

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<img src="https://media.giphy.com/media/xTcnSWYZvafyhEACBO/giphy.gif">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

@app.route("/hello/<username>/<int:number>")
def hello(username, number):
    return f"Hello Mr {username} you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)

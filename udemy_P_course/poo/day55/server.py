from flask import Flask
import random

app = Flask(__name__)

guessing_number = random.randint(0, 9)


@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def get_number(number):
    text = ""
    if number < guessing_number:
        text = '<h1 style="color:red">Too Low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > guessing_number:
        text = '<h1 style="color:purple">Too High, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        text = '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return text


if __name__ == "__main__":
    app.run(debug=True)

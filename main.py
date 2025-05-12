import random

from flask import Flask

gif = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
lower = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
higher = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
correct = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

app = Flask(__name__)

random_number = random.randint(0,10)

@app.route('/')
def homepage():
    return ('<h1>GUESS A NUMBER BETWEEN 0 AND 9:</h1>'
            f'<img src="{gif}"/>')

@app.route('/<int:answer>')
def answer(answer):
    if answer == random_number:
        return f'<h1>Correct! You got it! The answer is {answer}</h1> <br> <img src="{correct}"/>'
    elif answer > random_number:
        return f'<h1>Give a lower number</h1> <br> <img src="{lower}"/>'
    elif answer < random_number:
        return f'<h1>Give a higher number</h1> <br> <img src="{higher}"/>'


app.run(debug=True)

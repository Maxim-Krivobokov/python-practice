from flask import Flask
from vsearch import search4letters


app = Flask(__name__)  # __name__ - указатель на имя активного модуля


@app.route('/')   # вызов декоратора
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/123.htm')
def hello2() -> str:
    return 'New page in construction!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()

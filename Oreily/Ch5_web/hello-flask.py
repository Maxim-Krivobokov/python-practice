from flask import Flask
from vsearch import search4letters  # модуль vsearch - самодельный, установлен из архива с помощью pip


app = Flask(__name__)  # __name__ - указатель на имя активного модуля, точнее - ТЕКУЩЕЕ  АКТИВНОЕ ПРОСТРАНСТВО ИМЕН


@app.route('/')   # вызов декоратора, который дополняет нижеописанную функцию, для вывода на экран по URL = IP + '/'
def hello() -> str:
    return 'Hello world from Flask!'  # на экран будет выведена только эта строка


@app.route('/123.htm')
def hello2() -> str:
    return 'New page in construction!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()

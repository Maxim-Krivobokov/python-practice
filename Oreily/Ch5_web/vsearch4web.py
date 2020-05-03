from flask import Flask
from vsearch import search4letters
from flask import render_template, request, redirect


app = Flask(__name__)  # __name__ - указатель на имя активного модуля


@app.route('/')   # вызов декоратора
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')   # функция render_template возвращает html-файл, беря шаблон и аргументы


@app.route('/search4', methods=['POST'])  # указываем явно метод передачи - такой же как прописан в html-шаблоне (иначе будет ошибка)
def do_search() -> 'html':
    phrase = request.form['phrase'] # параметры берем из шаблона entry.tml, request.form возвращает значение, введенное в форму 'phrase'
    letters = request.form['letters']
    title = 'Here are your results: '
    # вызываем функцию из модуля vsearch
    results = str(search4letters(phrase, letters))
    # передаем функции render_template шаблон, и все аргументы
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results, )


app.run(debug=True)

from flask import Flask, escape
from vsearch import search4letters
from flask import render_template, request, redirect


app = Flask(__name__)  # __name__ - указатель на имя активного модуля

# функция записывает (добавляет) аргументы в логфайл
def log_request(req: 'flask_request', res: str) -> None:  # первый аргумент - переменная - html-запрос
    with open('vsearch.log', 'a') as logfile:
        #print(str(dir(req)), res, file=logfile)   # dir вернет все методы и атрибуты объекта req (request)
        print(req.form, file=logfile, end='|')
        print(req.remote_addr, file=logfile, end='|')
        print(req.user_agent, file=logfile, end='|')
        print(res, file=logfile, end='\n')







@app.route('/')   # вызов декоратора
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')   # функция render_template возвращает html-файл, беря шаблон и аргументы


@app.route('/search4', methods=['POST'])  # указываем явно метод передачи - такой же как прописан в html-шаблоне (иначе будет ошибка)
def do_search() -> 'html':
    phrase = request.form['phrase'] # параметры берем из шаблона entry.html, request.form возвращает значение, введенное в форму 'phrase'
    letters = request.form['letters']
    title = 'Here are your results: '
    # вызываем функцию из модуля vsearch
    results = str(search4letters(phrase, letters))
    # передаем функции render_template шаблон, и все аргументы
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results, )


@app.route('/viewlog')
def view_log() -> str:
    contents = []  # это будущий "вложенный " список
    with open('vsearch.log') as log:
        #  получаем из содержимого список списков:
        for line in log:  # разбираем каждую строку
            contents.append([]) #добавить новый пустой список в конец contents
            for item in line.split('|'):  # разбиваем каждую строку файла по спец разделителю
                contents[-1].append(escape(item))  # добавляем в последний список, в конец, элемент разделенной строки

        # менее оптимальные варианты:
        #contents = log.read()  # чтение файла целиком, присваивание переменной contents; неудобно - мешанина
        #contents = log.readlines() # прочесть все строки в файле в списокб спсиок из строк, не так удобно для обработки
    #return escape(contents)  # возвращаем экранированный (функция escape) список строк, чтобы не было путаницы со спецсимволами: <, >
    #return escape(''.join(contents)) # объедимяем список в одну юольшую строку
    return str(contents)


# запускаем только в главном пространстве имен, чтобы при использовании сторонних модулей -  AWS, например, которые сами запускают run - не было ошибок
if __name__ == '__main__':  
    app.run(debug=True)


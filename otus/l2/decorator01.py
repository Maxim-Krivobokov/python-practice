#


def a_func():
    print('Hello from a_func!')


a_func()

# we need the a_func() to print both 'some text', and hello message, like this:
print('some text')
a_func()

print('time to decorate'.center(50, '-'))

# for this we use decorator (name decorator01 can be any)

# берет в качестве аргумента функцию, которую нужно "допилить"


def decorator01(func):
    def wrapper():    # wrapper добавляет к исходной функции еще какие-то действия (вывод текста some text)
        print('Greetings to a new decorated function!')
        print('some text')
        func()
    return wrapper


# переназначили исходную функцию, теперь она выводит еще и 'some text'
a_func = decorator01(a_func)

print('new function: a_func modified'.center(50, '_'))
a_func()

# второй способ переназначить функцию
""" 
 таким образом вызываем декоратор, описанный выше, 
 для нижележащей функции b_func. 
 То есть b_func будет выводить 'some text', определенный во wrapper, и затем свой текст (hello from b_fucnt)

 """

print('new function: b_func'.center(50, '_'))
@decorator01
def b_func():
    print('another cool func, hello from b_funct')


b_func()

# декоратор в который передаются аргументы


def decorator02(func):
    def wrapper(x, y):   # передает туда все аргументы исходной функции
        print(x, y)  # выводит на экран аргументы
        return func(x, y)       # возвращает заданную функцию с аргументами
    return wrapper


def decorator03(func):
    def wrapper(*args):   # то же самое что и  wrapper(x, y) - передает туда все аргументы исходной функции
        print(args)  # выводит на экран аргументы, в виде кортежа
        return func(*args)       # возвращает заданную функцию с аргументами
    return wrapper


# base function count
def count(a, b):
    return a + b


print(count(3, 4))


print('decorated function: '.center(50, '-'))
# decorated function count()


@decorator02
def count_d(a, b):
    return a + b


print(count_d(3, 4))

print('another decorated function: '.center(50, '-'))
# decorated function count()


@decorator03
def count_c(a, b):
    return a + b


print(count_c(3, 4))


""" передача декоратору именованных аргументов  """

print('decorator with named arguments'.center(60, '='))


def decorator04(func):
    def wrapper(*args, **kwargs):   # kwargs = keyword args, именованные аргументы
        print('args: ')
        print(args)  # тип - кортеж
        print('kwargs: ')
        print(kwargs)  # тип - словарь
        return func(*args, **kwargs)
    return wrapper


@decorator04
def count_n(a, b):
    return a + b


# здесь функции передаются именованные аргументы, kwargs
print(count_n(a=7, b=5))

print('-------unnamed arguments-------------')
print(count_n(7, 5))  # здесь функции передаются НЕименованные аргументы, args

print('-------mixed  arguments-------------')
# здесь функции передаются  и именованные, и НЕименованные аргументы, kwargs и  args
print(count_n(7, b=5))

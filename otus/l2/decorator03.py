# создадим генератор декораторов


def gen_dec(x):
    print('Generator of decorators started.')

    def decorator01(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            # перемножаем результат выполнения функции на аргумент генератора
            return x * func(*args, **kwargs)
        print('Wrapper is generated!')
        return wrapper

    print('Decorator is generated!')
    return decorator01


# function to be decorated

def multiply(a, b):
    return a * b


print(multiply(3, 4))

print('calling a decorator gen:'.center(50, '-'))


@gen_dec(3)   # нужно передать генератору какое-то значение
def multiply_d(a, b):
    return a * b


# после первого вызова, уивдим сообщения генератора 'generator started', и.т.д
print(multiply_d(3, 4))
# со второго вызова и далее текстовых сообщений не будет
print(multiply_d(3, 4))
print(multiply_d(3, 4))
print(multiply_d(3, 4))

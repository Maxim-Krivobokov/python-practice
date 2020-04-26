from functools import wraps
# эта функция позволяет упростить конструкцию в логах

# создадим генератор декораторов
# этот генератор подставляет свой аргумент в функцию, которую теперь можно вызывать без него.


def gen_dec(x):
    print('Generator of decorators started.')

    def decorator01(func):
        # после вызова функции, задекорированной с помощью этого генератора, ее тип будет выглядеть проще
        @wraps(func)  # передается функция. которую декорируем
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            # передаем (подставляем) аргумент генератора в функцию, ей как раз его не хватает
            return func(x, *args, **kwargs)
        print('Wrapper is generated!')
        return wrapper

    print('Decorator is generated!')
    return decorator01


# function to be decorated

def multiply(a, b):
    return a * b


print(multiply(3, 4))

print('calling a decorator gen:'.center(50, '-'))


@gen_dec(5)   # нужно передать генератору какое-то значение
def multiply_d(z, a, b):
    print(z, a, b)
    return z + a * b


# на место первого аргумента (z) подставится x = 5, из декортатора. Получится 5 + 3* 4
print(multiply_d(3, 4))

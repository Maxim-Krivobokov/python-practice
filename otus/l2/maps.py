

""" map construction is for using function for every item  of the list"""


# better to use lambas instead of this short functions
def funct(x: int = 0):
    return x + 3


values = ['1', '2', '3', '4', '15']

# arguments are function amd list. Possible to use lambdas
map(funct(), values)

# this will return a map - object; 'generator-like' object
#map(lambda x: x + 3, values)

mapped = map(lambda x: x + 3, values)

print(mapped)

# can not print, bacause type = int
# print(str(list(mapped)))


def exp(x):
    return lambda y: y ** x


a = 2
# funcs is a generator
# using comprehension
# это генератор, возвращающий каждый раз функцию exp по возведению в  Х-ю степень числа У, где  Х от 2 до 6
funcs = (exp(x) for x in range(2, 6))
# этот map берет функцию и список функций exp(2-6) из funcs, и в качестве аргумента Y передает а = 2
map(lambda f: f(a), funcs)

# lambda f: f(a) нужна для того, чтобы передать "внутренней" функции аргумент а.

# этот объект будет списком из степеней числа А=2 : [4, 8, 16, 32]
list(map(lambda f: f(a), funcs))

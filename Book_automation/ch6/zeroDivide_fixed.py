def funct(divideBy):
    try:
        return 42 / divideBy  # this function takes a var and use it lika a divider
    except ZeroDivisionError:
        print('U cant devide by zero moron!')
print(funct(2))
print(funct(12))
print(funct(1))
print(funct(0))
print(funct(3))
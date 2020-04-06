def funct(divideBy):
    return 42 / divideBy  # this function takes a var and use it lika a divider
    

#this works too
try:
    print(funct(2))
    print(funct(12))
    print(funct(1))
    print(funct(0))  # this will cause an exception, and program will stop
    print(funct(3))   # this will not be printed

except ZeroDivisionError:
    print('U cant devide by zero moron!')
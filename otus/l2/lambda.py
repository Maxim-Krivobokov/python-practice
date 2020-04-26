""" Using lambda functions """

# function exp will return a function


def simple_exp():
    return lambda: 42


var01 = simple_exp()
print(simple_exp)
print(type(var01))

# calling inner function lambda, and it will print 42
print(simple_exp()())


# this function returns lambda -function, that takes Y and raises it to the power of X
def exp(x):
    return lambda y: y ** x


# exp_3 is function, that takes and argument raises it to the power of 3


exp_3 = exp(3)
print(exp_3(2))

print(exp(5)(3))

print('------------------------')


def gen():
    for i in range(10):
        print(i)
        if i > 5:
            return
        yield i


g = gen()

print(next(g))
print(list(g))

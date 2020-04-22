# examples with fucntions


def outer_funct():
    def inner_funct():
        return 'inner text'
    return inner_funct


print(outer_funct())

# this function is equal to inner_funct()
funct01 = outer_funct()

print(funct01)
print(funct01())

print(type(funct01))

# this is kind of constructor of functions


def mul_x(x):
    print('Got', x)

    def multiply(y):
        return x * y
    return multiply


# mul_3 is function that multiplies an argument (y) to 3
mul_3 = mul_x(3)

print(type(mul_3))


print(mul_3(5))
print(mul_3(8))
print(mul_3(15))

#

# yield statements returns a generator object


# this generator will work just once - with value = 42
def gen_broken():
    yield 42


print(gen_broken())


g1 = gen_broken()


# this will print 42
print(next(g1))

# this will cause an error - StopIteration
#  print(next(g1))


# this generator will return 5 values
def next_gen():
    for i in range(5):
        yield i


g2 = next_gen()

# we can print a list from generator object, but only once, and after that generator will be empty
# print(list(g2))

print(next(g2))
print(next(g2))
print(next(g2))


# this function is analog to enumerate()
#  set up default values
def our_enum(sequence, start=0):
    #n = 0
    n = start
    for item in sequence:
        yield n, item
        n += 1


print('Using function Our enum:')
values = ['2', '4', '6', '8', '10']

g3 = our_enum(values, 1)
g4 = our_enum(values)

print(g3)
print(list(g3))

print(list(g4))

# print(next(g3))
# print(next(g3))

# print(next(g4))
# print(next(g4))

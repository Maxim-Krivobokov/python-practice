""" function enumerate """

values = ['2', '4', '6', '8', '10']


enum = enumerate(values)

print(next(enum))

for i, val in enumerate(values):
    print(i, val)


for i, val in enumerate(values, 1):
    print(i, val)


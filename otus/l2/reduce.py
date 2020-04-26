from functools import reduce

reduce  # берет в аргументы функцию, и список

to_mul = range(1, 7)

# третий аргумент это опциональный множитель для итогового результата
product = reduce(lambda x, y: x * y, to_mul, 1)

# result is 1 * 2 * 3 * 4 * 5 * 6 ...etc
print(product)

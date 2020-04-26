""" function for calculating fibonacci numbers """


# without generator
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print('using fucntion fibonacci')
print(fib(100))

print(fib(65536))
print('-----------------------')

# using recursion, n is number in list of fibonacci numbers


def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)


print('using recursion function: ')
print(recur_fib(10))

def double(arg):
    print('Before double: ', arg)
    arg = arg * 2
    print('after double: ', arg)


def change(arg):
    print('Before change: ', arg)
    arg.append('More data')
    print('After change: ', arg)


object01 = 'Hello'
object02 = ['abc', 'def']

double(object01)
print(object01)
double(object02)


change(object02)
print(object02)

from contextlib import contextmanager

# функция для работы с контекстным менеджером


@contextmanager
def managed_res(*args, **kwargs):
    print(args, kwargs)
    yield 42
    print('Network closed')


# resource - результат вызова функции managed_res, которая возвращает 42.
with managed_res(1, 2, 3) as resource:
    print(resource, resource + 100)
    print('Leaving')

print('End')

print('==========================')


@contextmanager
def managed_res_new(*args):
    print(args)
    yield map(lambda x: x * 2, args)
    print('Network closed', args)


# g - это map, возвращаемый функцией managed_res_new
with managed_res_new(1, 2, 3) as g:
    print(list(g))
    print('Leaving')

print('End')

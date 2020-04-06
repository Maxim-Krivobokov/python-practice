# вызывается  глобальная переменная eggs, т.к одноименная локальная не определена


def spam():
    print(eggs)


eggs = 42
spam()
print(eggs)

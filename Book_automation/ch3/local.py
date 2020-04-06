# области видимости

# локальную переменную нельзя вызывать вне ее области, вне ее она не существует
# после заверпшения работы функции, ее локальная область со всеми лок. переменными уничтожается
#  глобальную можно вызывать откуда угодно
# в локальных областях не могут использоватся переменные из других лок областей
# в глобальной области исп только глобальные переменные


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0
    print(eggs)
    print(ham)


# переменные eggs в обоих функциях не связаны, т.к находятся в разных локальных областях

spam()

a = 7

b = 6

if a > b:
    value = a * 2
else: 
    value = b // 2
print('Value is', value)


#булевы операции и переменнные
TR1 = (a > 0 or b -10 > 0)
print(TR1)



results = []

values = [1, 2, 3, 4, 5]

#добавление в список  измененных элементов другого списка
for value in values:
    results.append(value ** 2)
print(results)

#вывод строки посимвольно
for char in 'abcdefg':
    print(char, end='  ')

#склейка строк
string = ''
strings = ['abc', 'def', 'ghi']
for s in strings:
    string += s
print(string)


#склеивание строк нормальное:
print(''.join(strings))


# другой пример фор
[val ** 2 for val in values]
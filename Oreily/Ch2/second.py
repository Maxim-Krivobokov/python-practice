values = [1, 2, 3, 4, 5]

lines = ['spam', 'eggs', 'cucumber']

#lines[: - это полный срез - копия переменной lines]
for line in lines[:]:
  if len(line) > 5:
    lines.insert(0, line)
print(lines)



line = 'python'

# срез с шагом 2
print(line[::2])

# срез с шагом 3
print(values[::3])

# срез с обрытнфм порядком
print(values[::-1])
print(line[::-1])



z = range(10)
y = range (5, 10)
#print(range(10))

list(range(0, 10))

print(z)
print(y)

values2 = list(range(7, 13))

#пробегаемся по всем элементам values2, выводим их номер и значение
for i in range(len(values2)):
  print(i, values2[i])


#распаковка tuple
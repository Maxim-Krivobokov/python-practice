

todos = open('todos.txt', 'a')

print('Feed the cat. ', file=todos)

print('Prepare tax return. ', file=todos)

print('Buy a beer.', file=todos)


# если не закрыть файл, данные будут утеряны
todos.close()
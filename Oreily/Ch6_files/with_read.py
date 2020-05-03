

# такой способ - компактная замена командам tasks = open(f.txt), <...>, tasks.close()
with open('todos.txt') as tasks: # открытие файла через управление контекстом. закрывать файл не нужно
    for line in tasks:
        print(line, end='')
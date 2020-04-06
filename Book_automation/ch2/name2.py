import sys
from random import random
name = ''

while True:
    print('Please type your name or exit.')
    name = input()
    if name == 'your name':
        break
    elif name == 'exit':
        sys.exit()  # выход из программы
print('Thank you')

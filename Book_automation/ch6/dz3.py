import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(number*3 +1)
        return  3 * number + 1

print('enter a number please')

try:
    startnum = int(input())
except ValueError:
    print('enter a number blyat\'')
    sys.exit()

#collatz(startnum)
current_num = startnum
while current_num != 1:
    current_num = collatz(current_num)

print('finish')


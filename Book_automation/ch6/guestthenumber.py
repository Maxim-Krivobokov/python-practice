# game of guessing numbers

import random
secretNumber = random.randint(1, 20)
print('I have chosen one number from 1 to 20. Try to guess what is it')

# give a player 6 tries to guess
for guessesTaken in range(1,7):
    print('enter your number')
    guess = int(input())

    if guess < secretNumber:
        print('Your number is less than target')
    elif guess > secretNumber:
        print('Your number is greater than target')
    else:
        break # when you answered right

if guess == secretNumber:
    print('You are right! Number of tries = ' + str(guessesTaken))
else:
    print('No. The right number was' + str(secretNumber))

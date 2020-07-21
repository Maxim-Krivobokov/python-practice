import random

guessesTaken = 0

print('Hello, what is your name?')

player_name = input()

number = random.randint(1,20)

print('I concieved a number')
for guessesTaken in range(6):
    print('Try to guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is too small')

    if guess > number:
        print('Your number is too large')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Congrats, ' + player_name + '! You have done it for ' + guessesTaken + ' tries.')

if guess != number:
    number = str(number)
    print('You loose. The number was: ' + number)


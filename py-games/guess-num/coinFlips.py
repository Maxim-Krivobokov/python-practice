import random

print('I \'ll   toss up  a coin 1000 times. Guess how many times an Eagle will appear. Press enter to start')

input()
flips = 0
heads  = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('90% completed, eagle appeared ' +  str(heads) + ' times.')

    if flips == 100:
        print('10% completed, eagle appeared ' + str(heads) + ' times.')

    if flips == 500:
        print('50% completed, eagle appeared ' + str(heads) + ' times.')

print()
print('From 1000 flips eagle was ' + str(heads) + ' times.')
print('How close were you to right answer?')


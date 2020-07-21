import random
import time

def displaytIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. в одной из них - дружелюбный дракон.
    В другой - злой, он вас сьест.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Choose a cave. (enter 1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach to the cave...')
    time.sleep(2)
    print('You are full of fear of the dark... ')
    time.sleep(2)
    print('Big dragon jumps towards you . he open his jaws and ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('..and he gives you some treasures!')
    else:
        print('And he bites your head off!')

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displaytIntro()
    caveNumber = chooseCave()
    #print(caveNumber)
    checkCave(caveNumber)

    print('Would you try your luck again? (yes or no)')
    playAgain = input()

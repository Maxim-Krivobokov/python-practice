import logging
import random

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

HANGMAN_PICS = ['''
      +---+
          |
          |
          |
         ===''',  '''
      +---+
      0   |
          |
          |
         ===''',  '''
      +---+
      0   |
      |   |
          |
         ===''',  '''
      +---+
      0   |
     /|   |
          |
         ===''',   ''' 
      +---+
      0   |
     /|\  |
          |
         === ''', '''
      +---+
      0    |
     /|\   |
     /     |
         === ''', '''
      +---+
      0    |
     /|\   |
     / \   |
         ===''']

words = 'book tree house tiger crocodile lion elephant'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    #logging.DEBUG('secret word is ' + str(secretWord))
    print('Wrong chars: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace __ with found chars
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] +  secretWord[i] + blanks[i+1:]

    for letter in blanks:   # shows secret word
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # returns a char, which was given by player.This function checks that input must be single character.
    while True:
        print('Enter a char.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter just a single letter.')
        elif guess in alreadyGuessed:
            print('You have already entered this letter. Chose other')
        elif guess not in 'abcdefghijklmnopqrstvuwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Doy you want to play again? ( Y // N)')
    return input().lower().startswith('y')   # returns true if typed Yes

print('HANGMAN')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range (len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('YES! Secret word is: ' + secretWord + ' You Won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        #check if player exceeded the limit of tries and lost
        if  len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You lost. Wrong letters: ' + str(len(missedLetters)) + 'Correct letters: ' + str(len(correctLetters)) + 'secret word: ' + secretWord)
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break




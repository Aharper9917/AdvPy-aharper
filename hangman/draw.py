import os

HANGMANSNIPS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
    /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
    / \  |
          |
    =========''']

def man(x):
    os.system('cls')
    print(HANGMANSNIPS[x])

def board(word, guesses):
    string = ""
    for c in word:
        if c == '-':
              string +='-'
        elif c in guesses:
              string += ' ' + c
        else:
          string += ' _'
    print(string)

def letters(letters, c):
    string = ""
    for letter in letters:
          string += ' ' + letter
    print('Guessed Letters:\n' + string + '\n')

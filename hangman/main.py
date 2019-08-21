'''
Allen Harper
CSCI 320: AdvProg Python

'''
import os
import random
from time import sleep
import draw


def randomWord():
    with open("words.txt", 'r') as wordFile:
        line = next(wordFile)
        for num, aline in enumerate(wordFile, 2):
            if random.randrange(num):
                continue
            line = aline.strip().lower()
    wordFile.close()
    return line

def gameover():
    os.system('cls')
    print('''
            _____                        _____                _ 
            |  __ \                      |  _  |              | |
            | |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __| |
            | | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
            | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |  |_|
            \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)''')

def win():
    os.system('cls')
    print('''
            __   __            _    _             _ 
            \ \ / /           | |  | |           | |
            \ V /___  _   _  | |  | | ___  _ __ | |
            \ // _ \| | | | | |/\| |/ _ \| '_ \| |
            | | (_) | |_| | \  /\  / (_) | | | |_|
            \_/\___/ \__,_|  \/  \/ \___/|_| |_(_) ''')

def checkWin(word, guessedLetters):
    tally = 0
    for letter in word:
        if letter in guessedLetters: tally += 1
        else: break
    if tally == len(word):
        return True

def run():
    print('Game Running...')

    word = randomWord()
    guess = " "
    guessedLetters = []
    numOfGuesses = 0

    while run:
        if numOfGuesses < 6:
            draw.man(numOfGuesses)
            draw.letters(guessedLetters, guess)
            draw.board(word, guessedLetters)

            print('\nEnter your guess.')
            guess = input("> ")
            guessedLetters.append(guess)

            # if guess not found, else guess found...
            if word.find(guess) == -1:
                numOfGuesses += 1
                print('\nWRONG!')
                if numOfGuesses != 6:
                    print('Try again.')
                    if numOfGuesses == 5:
                        print('One more guess!')
                        sleep(1)
                    sleep(2)
            else:
                print("\nCorrect!")
                sleep(2)
                if checkWin(word, guessedLetters):
                    win()
                    break
        else:
            gameover()
            break
    

def main():
    run()
    while input('Do you want to play again? (y/n)\n> ') == 'y':
        run()
    print("GOOD BYE!")
    
if __name__ == "__main__":
    main()

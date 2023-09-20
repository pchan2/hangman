from curses.ascii import isalpha

while True:
    guess = input('Guess a letter: ')
    if len(guess) and isalpha(guess):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
from curses.ascii import isalpha

import random

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('Guess a letter: ')
        if len(guess) == 1 and isalpha(guess):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

word_list = ['banana', 'grapes', 'watermelon', 'blueberry', 'carambola']
print(word_list)

word = random.choice(word_list)
print(word)
ask_for_input()
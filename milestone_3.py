from curses.ascii import isalpha

import random

word_list = ['banana', 'grapes', 'watermelon', 'blueberry', 'carambola']
print(word_list)

word = random.choice(word_list)
print(word)

guess = ''

while True:
    guess = input('Guess a letter: ')
    if len(guess) and isalpha(guess):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
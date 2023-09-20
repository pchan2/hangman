import random

word_list = ['banana', 'grapes', 'watermelon', 'blueberry', 'carambola']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('enter a single letter: ')
guess = guess.lower()
print(guess)
if len(guess) == 1 and 97 <= ord(guess) <= 122:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
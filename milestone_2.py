import random

word_list = ['banana', 'grapes', 'watermelon', 'blueberry', 'carambola']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('enter a single letter: ')
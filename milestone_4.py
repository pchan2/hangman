import random


class Hangman:

    def __init__(self, word_list: list, num_lives: int=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = self.initialise_word_guessed() # Characters guessed. ['_', '_', '_']
        self.num_letters = len(set([*self.word])) # The number of UNIQUE letters in the word that have not been guessed yet.
        self.list_of_guesses = [] # The list of characters guessed.

    def initialise_word_guessed(self) -> list:
        char_list = []
        for _ in self.word:
            char_list.append('_')
        return char_list


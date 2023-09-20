from curses.ascii import isalpha
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

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or len(guess) == 1 and not isalpha(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



hangman = Hangman(['apple', 'pear', 'banana', 'kiwi', 'grapes'])
hangman.ask_for_input()
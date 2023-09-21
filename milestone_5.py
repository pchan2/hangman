from curses.ascii import isalpha
import random


class Hangman:
    '''
    This class is used to represent a hangman.

    Attributes:
        _word_list (list): the list of words.
        _num_lives (int): the number of lives with a default value of five.
        _word (str): the word is randomly selected from _word_list.
        word_guessed (list): the word guessed is a list of letters guessed with the initial values of '_'.
        num_letters (int): the number of unique letters in the word that have not been guessed yet.
        list_of_guesses (list): the list of letters guessed.
    '''
    def __init__(self, word_list: list, num_lives: int=5) -> None:
        '''
        See help(Hangman) for accurate signature.
        '''
        self._word_list = word_list
        self._num_lives = num_lives
        self._word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self._word)
        self.num_letters = len(set([*self._word]))
        self.list_of_guesses = [] 
    
    def ask_for_input(self) -> None:
        '''
        This function is used to ask for input from the user.

        A valid input is a single alphabetical letter that has not been
        guessed before. The validated letter is then checked against the
        letters of the randomly generated word.
        '''
        guess = input("Guess a letter: ")
        if self.__is_valid_input(guess):
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)

    def __is_valid_input(self, guess: str) -> bool:
        list_of_guesses = self.list_of_guesses
        if len(guess) != 1 or len(guess) == 1 and not isalpha(guess):
            print("Invalid letter. Please, enter a single " +
                  "alphabetical character.")
        elif guess in list_of_guesses:
            print("You already tried that letter!")
        else:
            return True

    def __check_guess(self, guess: str) -> None:
        guess = guess.lower()
        word = self._word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            self.__update_word_guessed(word, guess)
            self.num_letters -= 1
        else:
            self._num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self._num_lives} lives left.")
    
    def __update_word_guessed(self, word: str, guess: str) -> None:
        for i in range(len(word)):
            if word[i] == guess:
                self.word_guessed[i] = guess


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game._num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game._num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break


word_list = ['strawberry', 'pear', 'banana', 'kiwi', 'watermelon']
play_game(word_list)

import random


class Hangman:
    '''
    This class is used to represent a hangman.

    Attributes:
        _word_list (list): the list of words.
        num_lives (int): the number of lives with a default value of five.
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
        self.num_lives = num_lives
        self._word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self._word)
        self.num_letters = len(set([*self._word]))
        self.list_of_guesses = [] 
    
    def ask_for_input(self) -> None:
        '''
        This function is used to ask for an input from the user.

        A valid input is a single alphabetical letter that has not been
        guessed before. The validated letter is then checked against the
        letters of the randomly generated word.
        '''
        guess = input("Guess a letter: ")
        if self.__is_valid_input(guess):
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)

    def __is_valid_input(self, guess: str) -> bool:
        '''Validate the input and return an boolean.'''
        list_of_guesses = self.list_of_guesses
        if len(guess) != 1 or len(guess) == 1 and not guess.isalpha:
            print("Invalid letter. Please, enter a single " +
                  "alphabetical character.")
        elif guess in list_of_guesses:
            print("You already tried that letter!")
        else:
            return True

    def __check_guess(self, guess: str) -> None:
        '''Check if the guess is in the random word.'''
        guess = guess.lower()
        word = self._word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            self.__update_word_guessed(word, guess)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def __update_word_guessed(self, word: str, guess: str) -> None:
        '''Update the word_guessed list if the guess is correct.'''
        for i in range(len(word)):
            if word[i] == guess:
                self.word_guessed[i] = guess
        print(self.word_guessed)


def play_game(word_list: list) -> None:
    '''
    This function is used to run the hangman game.

    Args:
        word_list (list): the list of words.
    '''
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        else:
            game.ask_for_input()


if __name__ == "__main__":
    word_list = ['strawberry', 'pear', 'banana', 'kiwi', 'watermelon']
    play_game(word_list)

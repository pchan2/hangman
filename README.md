# Hangman

[[TOC]]

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Learnings

1. `ord()` gives an [ASCII Decimal Code](https://www.asciitable.com/) of a character.
2. `random.choice()` generates a random item from a list.
3. `isalpha()` checks if a character is alphabetical.
4. Ensure there are no bugs in the code before committing.
5. Refactor ([reference](https://portal.theaicore.com/project/ccec2912-b0c5-4798-bcfd-21add0e658af)):
    - Eliminate Code Duplication: Identify repeated code blocks and refactor them into separate methods or functions. This promotes code reusability and reduces the likelihood of bugs
    - Single Responsibility Principle (SRP): Ensure that each method has a single responsibility, focusing on a specific task. If a method handles multiple concerns, split it into smaller, focused methods
    - Access Modifiers: Make methods private or protected if they are intended for internal use within the class and not externally accessible
    - Avoid Nested Loops: Minimize nested loops whenever possible to improve code efficiency and reduce complexity
    - Minimal Use of self: When writing methods in a class, only use self for variables that store information unique to each object created from the class. This helps keep the code organized and ensures that each object keeps its own special data separate from others
    - Consistent Docstrings: Provide clear and consistent docstrings for all methods, explaining their purpose, parameters, and return values. This aids code understanding for other developers
6. Docstring commands:
    - `help(Hangman) `# prints the class docstring, initialiser and public methods
    - `print(Hangman.__dir__)`
    - `print(Hangman.__dict__)`
    - `print(Hangman.__doc__)` # prints the class docstring

## Milestones

- [x] Set up the environment.
- [x] Create the variables for the game.
- [x] Check if the guessed character is in the word.
- [x] Create the Game Class.
- [x] Putting it all together.

## Installation

- [Python3](https://www.python.org/downloads/)

## Usage

1. Run `python3 milestone_5.py`
2. Enter a single alphabetical guess letter.
3. If the letter is invalid, you will be prompted to re-enter.
4. You have five lives in total.
5. To win, you have to guess the correct letters of a random word.
6. You will lose one life if your guess is wrong.
7. If you have used up your lives, you will lose.
8. To end the game prematurely, press `Ctrl`+`c` or `Ctrl`+`x`

## File structure of the project

**milestone_5.py:**

1. Imports of modules.
2. Hangman class definition.
    1. Initialiser.
    2. Public methods:
        - `ask_for_input`
    3. Private methods:
        - `__is_valid_input`
        - `__check_guess`
        - `__update_word_guessed`
3. `play_game` definition.
4. `word_list` initialisation.
5. `play_game()` execution.

## License

The MIT License (MIT)

Copyright (c) 2023 Patrick Chan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
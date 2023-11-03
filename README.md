# Hangman Game

- This game is built using python and is a simple fun game to play on the command line! The user is promopted to pick a single letter, in order to guess what a random word is. The user is given 5 lives, losing one if a wrong letter is guessed. Once the user guesses a correct letter, the word starts to form. If the user is able to guess all the letters, the word is outputed a success message is printed!

## Usage

- Create a list of words, and then create an instance and call the play_game() method to start the game!

```python

words = ["triangle", "square", "circle", "rectangle", "pentagon"]
game = Hangman(words)
game.play_game()

```

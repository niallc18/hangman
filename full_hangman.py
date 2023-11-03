import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):

        """
        Initialize a Hangman game with a word list and number of lives.

        Args:
            word_list (list): List of words to choose from.
            num_lives (int, optional): Number of lives the player starts with. Defaults to 5.
        """

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _check_guess(self, guess):

        """
        Check if a guessed letter is in the word and update game state.

        Args:
            guess (str): The guessed letter.
            word (str): The word to guess.
            word_guessed (list): List representing the guessed letters.
            num_letters (int): Number of unique letters remaining to guess.
            num_lives (int): Number of lives remaining.
        """

        guess = guess.lower()
        if guess in self.word:  
            print(f"Well done, you've guessed a correct letter, {guess} is in the word!")
            for pos, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[pos] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word, you have {self.num_lives} lives left!")

    
    def _ask_for_input(self):

        """
        Prompt the player for a letter guess and handle input validation.

        Args:
            word (str): The word to guess.
            list_of_guesses (list): List of previous guesses.
        """

        while True:
            guess = input("Guess a single letter: ")
            if (len(guess) != 1) or not (guess.isalpha()):
                print("Invalid letter, please enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!") 
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                return #...

    def play_game(self):

        """
        Main game loop to play Hangman.
        """

        while self.num_lives > 0 and self.num_letters > 0:
            print("Word guessed so far:", " ".join(self.word_guessed))
            print("Number of lives:", self.num_lives)
            print("List of guesses:", ", ".join(self.list_of_guesses))
            self._ask_for_input()

        if self.num_lives == 0:
            print("The game has ended, you've lost")
        elif self.num_letters == 0:
            print(f"Congratulations you've won! The word was {self.word}")


words = ["triangle", "square", "circle", "rectangle", "pentagon"]
game = Hangman(words)
game.play_game()
import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  
            print(f"Well done, you've guessed a correct letter, {guess} is in the word!")
            for char in self.word:
                if char == guess:
                    pos = self.word.index(char)
                    self.word_guessed[pos] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word, you have {self.num_lives} lives left!")

    
    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter: ")
            if (len(guess) != 1) or not (guess.isalpha()):
                print("Invalid letter, please enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!") 
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                return #end

    def play_game(self):
        while self.num_lives > 0 and self.num_letters > 0:
            print("Word guessed so far:", ' '.join(self.word_guessed))
            print("Number of lives:", self.num_lives)
            print("List of guesses:", ' '.join(self.list_of_guesses))
            self.ask_for_input()

        if self.num_lives == 0:
            print("The game has ended, you've lost")
        elif self.num_letters == 0:
            print(f"Congratulations you've won! The word was {self.word}")


words = ["triangle", "square", "circle", "rectangle", "pentagon"]
game = Hangman(words)
game.play_game()
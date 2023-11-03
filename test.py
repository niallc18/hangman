import random
word_list = ["apple", "kiwi", "pineapple", "blueberry", "bannana"]
word = random.choice(word_list)
empty = []
letters_of_word = list(word)

def ask_for_input():
    guess = input("Guess a single letter: ")
    return guess

def check_guess(guess):
    if guess in letters_of_word:
        letters_of_word.remove(guess)
        empty.append(guess)
        remaining = len(word) - len(empty)
        print(f"Well done, you've guessed a correct letter, {remaining} to go!")
    else:
        print("Good attempt, try another letter!")  
            


while True:
    if len(empty) == len(word):
        print(f"You've completed hangman! The word is {word}")
        break

    elif len(empty) < len(word):
        guess = ask_for_input()
        if (len(guess) == 1) and (guess.isalpha()):
            check_guess(guess)
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

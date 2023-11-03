import random

word_list = ["apple", "kiwi", "pineapple", "blueberry", "bannana"]
word = random.choice(word_list)
new = word.split(",")
print(new)
# guess = input("Enter a single letter: ")

# if (len(guess) == 1) and guess.isalpha():
#     print("Good guess!")
# else:
#     print("Oops! That is not a valid input")

# print(word_list)
# print(word)